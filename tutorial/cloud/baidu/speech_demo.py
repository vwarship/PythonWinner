from aip import AipSpeech

from tutorial.cloud.baidu import get_key_values


aipSpeech = AipSpeech(*get_key_values('speech_demo'))

text = '一条手链，一段奇缘。她是木府养女，天生废材，胆小懦弱，地位卑贱得连奴隶都不如，再次睁眼，眼中的胆怯早已不复存在。大婚前夕，她光明正大地逃，以一身极致医术毒术自立至心药铺。 ' \
       '本以为可以就此过上逍遥快活的日子，从此横行帝都，不成想一朝救了个神秘男子，便“后悔一生”。 人人尽说大夏朝皇帝冷漠无情，可是自己身后的霸道男人是个怎么回事？ 于是，某女千方百计地逃，却总被某人抓住，狠狠“惩罚”。 ' \
       '某男似笑非笑，丹凤眼微勾：木琬清，你再逃一次，朕让你三天下不了床。'
result = aipSpeech.synthesis(text, 'zh', 1, {
    'vol': 5,
    'per': 4,
})

if not isinstance(result, dict):
    with open('test.mp3', 'wb') as f:
        f.write(result)
