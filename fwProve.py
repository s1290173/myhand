import serial, time

PORT = "/dev/ttyAMA0"   # ← 実機のポート名に変更（例: /dev/ttyUSB0, /dev/ttyAMA0, COM7）
BAUD = 115200
ID   = 14               # 既定ID。変えている可能性があれば後のスキャナで探索

def crc16_modbus_little(data: bytes) -> bytes:
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    # ModbusはLow-byte→High-byte
    return crc.to_bytes(2, "little")

with serial.Serial(PORT, BAUD, timeout=0.6, write_timeout=0.6) as ser:
    # 読み取り系コマンドの方が成功しやすい（Code=0x03）
    # 「FW Major Version」を読む: Instruction(=1)
    pkt_wo_crc = bytes([0xFE,0xFE,0x08, ID, 0x03, 0x00, 0x01, 0x00, 0x00])
    tx = pkt_wo_crc + crc16_modbus_little(pkt_wo_crc)

    ser.reset_input_buffer(); ser.reset_output_buffer()
    ser.write(tx); ser.flush()
    time.sleep(0.12)

    rx = bytearray()
    deadline = time.time() + 1.0
    while len(rx) < 11 and time.time() < deadline:
        chunk = ser.read(11 - len(rx))
        if chunk: rx.extend(chunk)
        else: time.sleep(0.02)

    print("TX:", tx.hex())
    print("RX:", bytes(rx).hex(), "len=", len(rx))

    if len(rx) == 11:
        body, crc = bytes(rx[:9]), bytes(rx[9:])
        ok = (crc == crc16_modbus_little(body))
        print("CRC OK:", ok)
        if ok:
            # 応答のデータ部 7,8 バイトが値（high,low）。FW=1なら 00 01
            val = int(body.hex()[14:18], 16)
            print("FW Major =", val)
