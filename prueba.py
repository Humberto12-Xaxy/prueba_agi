from asterisk.agi import AGI

agi = AGI()

agi.answer()
resp = agi.stream_file()


