import asyncio, websockets, os, json

connected_users = []

def handleError(webhook, code, message):
	await websocket.send(f'{"code":"{code}","message":"{message}"}'.encode())

async def CHS(websocket, path):
	try:
    	stuff = await websocket.recv()
    	stuff = json.loads(stuff.decode())
    	os.system('clear')
    	print(stuff)
    	user_id = stuff['client_id'];event = stuff['event'];content = stuff['content']
    	print(f"\n\nUser ID is: {user_id}\nThe event type is {event}\nThe content of the message is '{content}'")
    	if event == 'connect':
        	connected_users.append(user_id)

    	await websocket.send('200'.encode())
	except Exception as e:
		await websocket.send(f'{"code":"500","message":"{e}"}'.encode())

    try:
        if user_id not in connected_users:
            #What should i put here as an error? I can make my own errors aswell









start_server = websockets.serve(CHS, "0.0.0.0")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()