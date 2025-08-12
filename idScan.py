import serial, time

PORT = "/dev/ttyUSB0"
BAUD = 115200
ID_RANGE = range(1, 255)   # 時間短縮したいなら range(1,50) など

def crc16_modbus_little(data: bytes) -> bytes:
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return crc.to_bytes(2, "little")

def probe_id(ser, id_):
    pkt = bytes([0xFE,0xFE,0x08, id_, 0x03, 0x00, 0x04, 0x00, 0x00])  # 「ID読み出し」
    pkt += crc16_modbus_little(pkt)
    ser.reset_input_buffer(); ser.reset_output_buffer()
    ser.write(pkt); ser.flush()
    time.sleep(0.08)
    rx = ser.read(11)
    if len(rx) == 11:
        body, crc = rx[:9], rx[9:]
        if crc == crc16_modbus_little(body):
            # 返ってきたID値
            val = int(body.hex()[14:18], 16)
            return val
    return None

with serial.Serial(PORT, BAUD, timeout=0.3, write_timeout=0.3) as ser:
    found = []
    for i in ID_RANGE:
        val = probe_id(ser, i)
        if val is not None:
            print(f"Responded at target {i} → Reported ID {val}")
            found.append((i, val))
            # 見つかったら十分ならbreakしてOK
    print("Found:", found)
