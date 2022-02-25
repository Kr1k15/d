import discord
import random
from discord.ext import commands

import requests
import io

client = commands.Bot( command_prefix = '.' )
client.remove_command( 'help' )
# .Привет

@client.event

async def on_ready():
  print( 'BOT connected' )

  await client.change_presence( status = discord.Status.online, activity = discord.Game( 'Нужна помощь? .help' ) )

@client.event
async def on_command_error( ctx, error ):
  pass

@client.command( pass_context = True ) 

async def Привет( ctx ):
  author = ctx.message.author
  await ctx.send( f' { author.mention } Привет. Я бот для вашего дискорд сервера. Создатель меня Kr1k#4018' )

#.say Пока пока
# > Пока пока

@client.command( pass_context = True )

async def say( ctx, arg, ):
  await ctx.send ( f' ' + arg )

#Clear message
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def clear( ctx, amount : int ):
  await ctx.channel.purge( limit = amount )
#.clear

#.kick
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None ):
  emb = discord.Embed( title = 'Kick', colour = discord.Color.red() )
  await ctx.channel.purge( limit = 1 )

  await member.kick( reason = reason )

  emb.set_author( name = member.name, icon_url = member.avatar_url )
  emb.add_field( name = 'Кикнут участник', value = 'Kicked user : {}'.format( member.mention ) )

  await ctx.send ( embed = emb )

  #await ctx.send( f'Кикнут участник { member.mention }' )

#.бан
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None ):
  emb = discord.Embed( title = 'Ban', colour = discord.Color.red() )
  await ctx.channel.purge( limit = 1 )

  await member.ban( reason = reason )

  emb.set_author( name = member.name, icon_url = member.avatar_url )
  emb.add_field( name = 'Забанен участник', value = 'Banned user : {}'.format( member.mention ) )

  await ctx.send( embed = emb )

  #await ctx.send( f'Забанен участник { member.mention }' )

#.mute
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def mute( ctx, member: discord.Member ):
  await ctx.channel.purge( limit = 1 )

  mute_role = discord.utils.get( ctx.message.guild.roles, name = 'mute' )

  await member.add_roles( mute_role )
  await ctx.send( f'У { member.mention } ограничение чата, за нарушение правил!' )

@clear.error
async def clear_error( ctx, error ):
   if isinstance( error, commands.MissingRequiredArgument ):
     await ctx.send( f'{ ctx.author.mention }, Обязательно укажите число!' )  

   if isinstance( error, commands.MissingPermissions ):
      await ctx.send ( f'{ ctx.author.mention }, у вас недостаточно прав!' )
    
@ban.error
async def ban_error( ctx, error ):
  if isinstance( error, commands.MissingPermissions ):
    await ctx.send ( f'{ ctx.author.mention }, у вас недостаточно прав!' )

#Conect 
token = open ( 'shad.txt', 'r' ).readline()

client.run( token )
