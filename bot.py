import discord
from discord.ext import commands
from discord.utils import get
import io
import aiohttp

TOKEN = 'NzEyNTg4MDkxMzQ0NDIwOTM1.XsTw4g.JUzqovwpc8KH9YlGEBNRw55LtVY'

client = commands.Bot( command_prefix= '.' )
client.remove_command( 'help' )
# .help

# Команды
#Приветствие
hello_words = ['hello', 'hi', 'Здарова']
hello_word = ['ky', 'ku', 'Hello' 'Привет']
Helloo = ['здарова', 'привет']
#Информация
answer_words = [ '.Какая информация', '.какая информация', '.какая информация о сервере' , '.Узнать информация о сервере', '.команды' ]
answer_world = [ '.Команды', '.какие команды' , '.команды сервера', '.Команды сервера', '.что здесь делать' ]
#Прощение
goodbye_words = ['пока', 'Пока', 'пока всем']
goodbye = ['bb', 'bb all', 'goodbye']
goodbyes = ['удачи всем', 'удачи']
#Как дела
wopros = ['.как дела ?']
woproos = ['.как дела' ]
#Что делаешь
woprosu = ['.что делаешь']
wopross = ['.что делаешь ?']
#Личные вопросы №1
no = [ '.Какой у тебя размер груди ?', '.Какой у тебя размер груди' ]
yes = [ '.какой у тебя размер груди','.какой у тебя размер груди?' ]
#Личные вопросы №2
noo = [ '.Сколько тебе лет ?', '.Сколько тебе лет']
Yees = [ '.cколько тебе лет', 'cколько тебе лет ?' ]

#Флуд
ploxo = [ 'сука', 'Сука', 'Cuka', 'cuka', 'cyka', 'Cyka', 'иду нахуй', 'иди в баню', 'пошел нахуй', 'Пошел нахуй', 'Пошол нахуй', 'пошел нахуй', 'пошел нахер', 'иди нахер', 'бля', 'Бля', 'блять', 'блядь', 'хер', 'Член' ]


#Подключение бота
@client.event

async def on_ready():
    await client.change_presence( status = discord.Status.idle, activity= discord.Game( 'World of Tanks' ) )
    print( 'Bot connected' )


@client.event
async def on_command_error( ctx, error ):
    pass

#Чистка
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def clear( ctx, amount : int ):
    await ctx.channel.purge(limit = amount)
    await ctx.send( embed = discord.Embed(description= f'Удалено {amount} сообщений', color = 0x07a28e))

    print( 'Была использована команда .clear' )

#кик 
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None ):
    emd = discord.Embed( title = 'Kick', colour = discord.Color.red() )
    await ctx.channel.purge( limit = 1 )

    await member.kick( reason= reason )

    emd.set_author( name = member.name, icon_url = member.avatar_url )
    emd.add_field( name = 'Kick user', value = 'Kick user : {} '. format( member.mention ) )
    emd.set_footer( text= 'Был кикнут админом {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )

    await ctx.send( embed = emd )

#бан
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None ):
    emd = discord.Embed( title = 'Ban', colour = discord.Color.red() )
    await ctx.channel.purge( limit = 1 )

    await member.ban( reason= reason )

    emd.set_author( name = member.name, icon_url = member.avatar_url )
    emd.add_field( name = 'Ban user', value = 'Baned user : {} '. format( member.mention ) )
    emd.set_footer( text= 'Был забанен админом {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )

    await ctx.send( embed = emd )

#антибан
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def unban( ctx, *, member ):
    await ctx.channel.purge( limit = 1 )

    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban( user )
        await ctx.send( f'Unbanned user { user.mention }' )

        return


#Ответы
@client.event

async def on_message( message ):
    await client.process_commands(message)
    msg = message.content.lower()
#Приветствие

    if msg in hello_words:
        await message.channel.send('Приветик мой семпай! ' )

    if msg in hello_word:
        await message.channel.send( 'Приветик , я рада тебя видеть!' )

    if msg in Helloo:
        await message.channel.send( 'Привет , я рада, что ты тут!' )
#.Help

    if msg in answer_words:
        await message.channel.send( 'Пропиши в чат команду .help, и всё узнаешь! 😇' )

    if msg in answer_world:
        await message.channel.send( 'Всё просто, напиши команду .help и узнаешь всё, что нужно' )
#Прощение

    if msg in goodbye_words:
        await message.channel.send( 'удачи тебе!' )

    if msg in goodbye:
        await message.channel.send( 'Приходи ещё!' )

    if msg in goodbyes:
        await message.channel.send( 'Пока пока!' )
#Как дела

    if msg in wopros:
        await message.channel.send( 'Отлично' )

    if msg in woproos:
        await message.channel.send( 'Хорошо' )
#Что делаешь

    if msg in woprosu:
        await message.channel.send( 'Я жду пока мой хозяин доделает меня ' )

    if msg in wopross:
        await message.channel.send( 'Жду, когда мой хозяин закончит со мной работу' )
#Личные вопросы №1
    if msg in no:
        await message.channel.send( 'Семпай ты пошляк!! 😡 ' )

    if msg in yes:
        await message.channel.send( 'Извращенец!!' )
#Личные вопросы №2
    if msg in noo:
        await message.channel.send( 'Это секрет 😜 ' )

    if msg in Yees:
        await message.channel.send( 'В тюрячку хочешь?' )
#Фильтр
    if msg in ploxo:
        await message.delete()
        await message.author.send( f'{ message.author.name }, не надо такое писать! ' )


#
@client.event

async def on_member_join ( member ):
    channel = client.get_channel( 547780865657143306 )

    role = discord.utils.get( member.guild.roles, id = 684041549918502914 )

    await member.add_roles( role )
    await channel.send( embed = discord.Embed( description = f'Пользователь ``{ member.name }``, присоеденился к нам!', color = 0x4B0082) )


@client.command()
async def send_a( ctx ):
    await ctx.channel.purge( limit = 1 )
    await ctx.author.send( 'Приветик' )


@client.command()
async def send_m( ctx, member: discord.Member ):
    await member.send( f'{ member.name }, привет от { ctx.author.name }')


#аргументы
@client.command( pass_context = True )

async def bot( ctx, arg):
    await ctx.channel.purge( limit = 1 )
    author = ctx.message.author

    await ctx.send( f' { author.mention } ' + arg )

@client.command( pass_context = True )

async def hello( ctx, amount = 1 ):
    await ctx.channel.purge( limit = amount )
    
    author = ctx.message.author
    
    await ctx.send( f'Приветик { author.mention } ')


#help
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def help( ctx ):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed( title = 'Список команд' )

    emb.add_field( name = '{}clear' .format( '.' ), value = 'Очистка чата 🧹' )
    emb.add_field( name = '{}kick' .format( '.' ), value = 'Кик участника 🔏' )
    emb.add_field( name = '{}ban' .format( '.' ), value = 'Бан участника 🔐' )
    emb.add_field( name = '{}unban' .format( '.' ), value = 'Анти бан участника 🔑')
    emb.add_field( name = '{}send_a @ник' .format( '.' ), value = 'Бот поприветствует участника(лс) 💓')
    emb.add_field( name = '{}send_m @ник' .format( '.' ), value = 'Бот поприветствует участника с твоим упоминанием(лс) 💌 ')

    await ctx.send( embed = emb )

#error
@clear.error 
async def clear_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент!' )

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав!' )

@ban.error
async def ban_error( ctx, error ):
    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав!' )

@kick.error
async def kick_error( ctx, error ):
    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав!' )

@unban.error
async def unban_error( ctx, error ):
    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав!' )

client.run( TOKEN )