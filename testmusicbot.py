import discord
import os
import asyncio
import youtube_dl

token = "MTA1MjExMTY3Mjg0NTgxMTc0Mg.GZ2qo8.-3ntrymfXEhXkrP_8fz_aL2BCcz-frNVeKZwNo"

client = discord.Client()

voice_clients = {} 

yt_dl_opts={'format':'bestaudio/best'}
ytdl=youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options={'options':"-vn"}


@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(msg):
    if msg.content.startswith("?play"):
        try:
            url = msg.content.split()[1]

            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client

            loop= asyncio.get_event_loop()
            data=await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

            voice_client.play() 

        except Exception as err:
            print(err)

client.run(token)