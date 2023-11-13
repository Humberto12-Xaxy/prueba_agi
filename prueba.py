from asterisk.agi import AGI

agi = AGI()

agi.answer()
agi.stream_file()