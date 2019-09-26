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

bot_token = 'NjA4Mjk0NDA5MDg3NDgzOTE0.XYwdfA.CgAoYcLEw0hsw-ijQ210cf9Sn-0'
self_bot_token = 'NTE2ODYxNTczOTIzNDcxNDAx.XXTa1g.tvjdmZxgrMJfwnmn-IO6bVQfxNc'

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '617582752539213824')

input_loco_private  = [
    "600283628726910976",
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
input_loco_public = ['608262001650696202']
command_channel = '608262001650696202' #trivia-answers
admin_chat = '620777556576305155' # answers2

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
