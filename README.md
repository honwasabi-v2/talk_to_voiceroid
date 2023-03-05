# talk_to_voiceroid
●プログラム説明
AIとVOICEROIDで会話するpythonプログラム

●内容
openAIAPI.py:	openAIのAPIを利用して文字列から返答を用意し，返答を成形する(ChatGPTではない)．
talkAPI.py:		RECRUITのA3RT APIを利用して文字列から返答を用意し，返答を成形する．
speech_to_text.py:	音声をpyaudioを用いて処理する．音声をoutput.wavに保存し，wavファイルからテキストにする．
text_to_speech.py:	pyvcroid2を用いて文字列をVOICEROIDに発声させる
voiceroid_talk.py:	メインで実行するファイル．各種コマンドもここ．

●実行に必要なもの
・RECRUITのA3RTかopenAIのAPIKey
・VOICEROID2本体
・pyvcroid2 (https://github.com/Nkyoku/pyvcroid2)
・他ライブラリ(requests，openai，sys，threading，time，winsound，numpy，pyaudio，wave，speech_recognition)
・python(私の環境では32bit版でしか動かなかった)

●実行方法
1.	各種ライブラリとAPIKeyを用意する
2.	voiceroid_talk.pyを実行
3.	会話するキャラクターを数字で入力
4.	どのAPIを使うかを数字で選択
5.	APIKeyを入力
6.	recordingと表示されたら```はきはきと'''しゃべる
7.	読み取られた言葉が表示され，please wait...(選択したAPI)...と表示されるので少し待つ
8.	VOICEROIDが読み上げてくれる
9.	6-8を繰り返す．
10.	終了するためには`終了'と発言する


●コマンド一覧
キーボード入力用：
	-EXIT，-q		:終了
	-openAIAPI	:openAIに切り替え
	-talkAPI		:A3RTに切り替え
	-help，-h，-list	:コマンド一覧表示
	-say		:音声入力に切り替え
	-chara		:読み上げキャラクター切り替え
音声入力用:
	終了		:終了
	キーボード		:キーボード入力に切り替え
	


