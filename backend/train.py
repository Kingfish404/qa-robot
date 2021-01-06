from robot.lib.chatterbot.chat import mybot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


trainer = ChatterBotCorpusTrainer(mybot)

trainer.train(
    "erkesets"
)
