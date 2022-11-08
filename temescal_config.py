#! /usr/bin/env python3

import sys
import temescal
import time
import yaml

def cb_func(response) -> None:
	print(yaml.dump(response, default_flow_style=False))

def main(speaker_ip: str) -> None:
	print("calling functions for [%s]" % speaker_ip)
	speaker = temescal.temescal(speaker_ip, 9741, cb_func)
	msgs = ["AVS_AUTH_DATA",
			"AVS_META_DATA",
			"C4A_SETTING_INFO",
			"CALIBRATION_VIEW_INFO",
			"DIAG_INFO",
			"EQ_VIEW_INFO",
			"FACTORY_SET_REQ",
			"FUNC_VIEW_INFO",
			"MSG_PARSING_ERROR",
			"PLAY_INFO",
			"PRODUCT_INFO",
			"RADIO_VIEW_INFO",
			"SETTING_VIEW_INFO",
			"SHARE_AP_INFO",
			"SPK_LIST_VIEW_INFO",
			"TEST_TONE_REQ",
			"UPDATE_VIEW_INFO"]
	for msg in msgs:
		speaker.send_packet({'cmd': 'get', 'msg': msg})
		time.sleep(1)

if __name__ == '__main__':
	main(sys.argv[1])

