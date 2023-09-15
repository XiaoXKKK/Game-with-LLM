import requests

WORKSPACE_ID = 'cyber-psychosis'
YOUR_KEY_HERE = '***REMOVED***'

url = 'https://studio.inworld.ai/v1/workspaces/{WORKSPACE_ID}/characters/test:simpleSendText'
headers = {"Content-Type": "application/json", "authorization": "Basic {YOUR_KEY_HERE}"}
myobj = {"character":"workspaces/{WORKSPACE_ID}/characters/test", "text":"hello there!", "endUserFullname":"Tom", "endUserId":"12345"}

x = requests.post(url, json = myobj, headers=headers)

print(x)


'''
curl -X POST https://studio.inworld.ai/v1/workspaces/cyber-psychosis/characters/test:simpleSendText \
-H 'Content-Type: application/json' \
-H 'authorization: Basic ***REMOVED***' \
-d '{"character":"workspaces/cyber-psychosis/characters/test", "text":"hello there!", "endUserFullname":"Player", "endUserId":"1"}'
'''
