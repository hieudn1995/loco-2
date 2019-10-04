import discord

def  init():
    global bot_token
    global self_bot_token
    global message
    global embed
    global output_channel
    global input_channel
    global command_channel

    global game_in_session
    global counter_public_1
    global counter_public_2
    global counter_public_3
    global counter_private_1
    global counter_private_2
    global counter_private_3
    global counter1
    global counter2
    global counter3
    global weight
    global weight_time
    global seconds_elapsed

bot_token = 'NjA4Mjk0NDA5MDg3NDgzOTE0.XZclZA.8QC_72uzSjKIR23yleJ3nk5oMYA'
self_bot_token = 'NTc3NTE1MjYzNzA5MjgyMzA1.XZcoJA.q77im1GyfolxANscDII7SXiYTX0'

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '608289976542691347')

input_loco_private  = [
    "608262001650696202",
    "593104881888264204",
    "593990608914219008",
    "569420128794443776",
    "569420198717816852",
    "459842150323060736",
    "523359669280833536",
	"535628205139296256",
	"525131707410677761",
	"513818250652680213",
	"544381529829146645",
    "569843705654149130",
    "566979656083963918", # answers1
    "559442345674670082", #answers2
    '559357612068700183' #trivia-answers
]
input_loco_public = ['608289976542691347']
command_channel = '608289976542691347' #trivia-answers
admin_chat = '608260358490030092' # answers2

game_in_session = False
counter_public_1 = 0
counter_public_2 = 0
counter_public_3 = 0
counter_private_1 = 0
counter_private_2 = 0
counter_private_3 = 0
counter1 = 0
counter2 = 0
counter3 = 0
weight = 5
weight_time = 1
wronggone1 = 0
wronggone2 = 0
wronggone3 = 0

seconds_elapsed = 0
