import orm
from models import User,Blog,Comment
import asyncio

async def test(loop):
	await orm.create_pool(loop=loop,user='root',password='root',db='awesome')
	u = User(name='Test',email='test@example.com',password='1234567890',image='about:blank')
	await u.save()
	await orm.destroy_pool()
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()