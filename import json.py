import json 

active_data = '''
{
	"agreements": [
		{
			"can_disconnect_packages": true,
			"serial_number": "None",
			"agreement_id": "72155567",
			"active": true,
			"can_create_xtraview": false,
			"device_name": "None",
			"account_friendly_name": "None",
			"can_query_showmax_subscription": false,
			"can_break_xtraview": false,
			"can_change_packages": true,
			"is_switched": "None",
			"can_cancel_showmax": false,
			"account_number": "None",
			"model": "None",
			"is_child_device": "None",
			"can_holiday_home_switch": false,
			"can_suspend_packages": false,
			"packages": [
				{
					"name": "SHOWMAXADDONPL",
					"description": "DStv Showmax Premier League Add-on",
					"agreement_type": "OTT",
					"type": "showmax",
					"status": "Active",
					"product_id": "126075479",
					"quantity": "1"
				},
				{
					"name": "SHOWMAXADDON",
					"description": "DStv ShowMax Add-on",
					"agreement_type": "OTT",
					"type": "showmax",
					"status": "Request Disconnect",
					"product_id": "126075478",
					"quantity": "1"
				},
				{
					"name": "COMPKUOTT",
					"description": "DStv Stream Compact",
					"agreement_type": "OTT",
					"type": "principal",
					"status": "Active",
					"product_id": "126075477",
					"quantity": "1"
				}
			],
			"linked_smartcard_serial_number": "None",
			"can_insure_decoder": false,
			"is_insured": "None",
			"model_description": "None",
			"agreement_type": "OTT",
			"agreement_actions": [
				{
					"action_title": "Disconnect Packages"
				},
				{
					"action_title": "Cancel Showmax EPL"
				},
				{
					"action_title": "Showmax EPL Activation Link"
				},
				{
					"action_title": "Change Packages"
				},
				{
					"action_title": "Reconnect Packages"
				},
				{
					"action_title": "Link Addon Package"
				}
			],
			"can_holiday_home_switch_back": false,
			"can_cancel_decoder_insurance": false,
			"can_reconnect_packages": true,
			"ott_package": true,
			"can_link_packages": true,
			"get_quote": false,
			"switch_back_date": "None"
		}
	],
	"status_code": 200
}'''

#From the Json above, get a list of package descriptions, where the status is active

active_packages=json.loads(active_data)
active_package= [
    package["description"] 
    for agreement in active_packages["agreements"]
    for package in agreement["packages"]
    if package["type"] != "showmax"
]
print(active_package)