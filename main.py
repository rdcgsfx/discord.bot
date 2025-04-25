import os
import discord
from discord.ext import commands
from discord import app_commands

from Myserver import sever_on

# กำหนด Intents สำหรับให้ Bot สามารถทำงานกับสมาชิกได้
intents = discord.Intents.default()
intents.members = True  # เปิดการใช้งาน event สมาชิกใหม่

# กำหนด prefix ของคำสั่ง Bot
bot = commands.Bot(command_prefix="!", intents=intents)

# event เมื่อ Bot พร้อมทำงาน
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# event ต้อนรับสมาชิกใหม่
@bot.event
async def on_member_join(member):
    # ส่งข้อความยินดีต้อนรับเมื่อสมาชิกใหม่เข้ามา
    channel = discord.utils.get(member.guild.text_channels, name="general")  # เปลี่ยนเป็นชื่อช่องที่คุณต้องการ
    if channel:
        # ส่งข้อความยินดีต้อนรับ
        message = await channel.send(f"🌟✨ยินดีต้อนรับทุกท่าน°.⇢ ˗ˏˋ{member.mention}࿐ྂ สู่โลกแห่งการไขปริศนาในคฤหาสน์หลังใหญ่ 🔍\n"
                                     f"เจ้าก้าวเข้าสู่โลกที่ความลับและความจริงซ่อนอยู่ในทุกมุมมืดของคฤหาสน์นี้ 🕵️‍♂️\n"
                                     f"ท่านจะต้องใช้ไหวพริบและความกล้าหาญในการค้นหาคำตอบ... ทุกก้าวที่เดินจะพาเจ้าหมุนวนใกล้ความจริงที่ยังคงลึกลับ 🌑✨\n"
                                     f"หวังว่าทุ่านจะเพลิดเพลินไปกับการไขปริศนา"
                                     f"--------------------------------\n"
                                     f"อ่านกฎได้ที่📢 : #̗̀➛อ่านกฎได้ที่｡･ﾟﾟ･\n"
                                     f"อ่านบทบาทได้ที่🍀 : #『บทบาท』\n"
                                     f"กดรับยศได้ที่🗝️ : #┊รับยศ┊➶｡˚°\n"
                                     f"ยกตัวอย่างแบบฟอร์ม📣 : #˚₊·-͟͟͞➳❥ตัวอย่างแบบฟอร์ม\n")

        # ส่งข้อความให้สมาชิกใหม่เลือกอิโมจิเพื่อรับยศ
        await message.add_reaction("🌻")  # กด 🌻 เพื่อรับยศ

    # event เมื่อมีการกดอิโมจิ
@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "‍🌻":
        role = discord.utils.get(user.guild.roles, name="Newcomer")
        if role:
            member = user
            await member.add_roles(role)  # มอบยศให้กับผู้ที่กด ‍🌻

server_on()

# เริ่มทำงานของ Bot
bot.run(os.getenv('TOKEN'))
