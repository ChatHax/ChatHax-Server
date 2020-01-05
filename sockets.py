
import asyncio, websockets, os, json
from exceptions import *
async def handleError(websocket, code, message):
	await websocket.send(str('{') + str(f'"code":"{str(code)}","message":"{str(message)}"') + str("}").encode())
'''
connected_users = []



async def CHS(websocket, path):
	try:
		stuff = await websocket.recv()
		stuff = json.loads(stuff.decode())
		print(stuff)
		user_id = stuff['client_id'];event = stuff['event'];content = stuff['content']
		print(f"\n\nUser ID is: {user_id}\nThe event type is {event}\nThe content of the message is '{content}'")
		if event == 'connect':
			if user_id in connected_users:
				del(connected_users[user_id])
			connected_users.append(user_id)
		elif event == 'message_send':
			pass #print("")

		await websocket.send('200'.encode())
	except Exception as e:
		await handleError(websocket, 500, e)
	try:
		if user_id not in connected_users:
			await handleError(webhook, 400, "Not connected")
			raise ClientNotConnected('Not connected')
			return
	except: 
		pass


start_server = websockets.serve(CHS, "0.0.0.0")

if __name__ == '__main__':
	print("Starting server")
	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()
'''
async def handle(websocket, path):
	try:
		stuff = str(await websocket.recv())
		stuff = json.loads(stuff.decode())
		print(stuff)
		user_id = stuff['client_id'];event = stuff['event'];content = stuff['content']
		print(f"\n\nUser ID is: {user_id}\nThe event type is {event}\nThe content of the message is '{content}'")
		if event == 'connect':
			if user_id in connected_users:
				del(connected_users[user_id])
			connected_users.append(user_id)
		elif event == 'message_send':
			pass #print("")

		await websocket.send('200'.encode())
	except Exception as e:
		await handleError(websocket, 500, e)
	try:
		if user_id not in connected_users:
			await handleError(webhook, 400, "Not connected")
			raise ClientNotConnected('Not connected')
			return
	except: 
		pass


class Server:

	def start(self):
		return websockets.serve(self.handler, '0.0.0.0') #we dont need a port but ok

	async def handler(self, websocket, path):
		async for message in websocket:
			await handle(websocket, path)
			print(f'server received :{message.decode()}')
			await websocket.send(f"Received: {message.decode()}".encode())

if __name__ == '__main__':
	print("Starting")
	ws = Server()
	asyncio.get_event_loop().run_until_complete(ws.start())
	asyncio.get_event_loop().run_forever()
