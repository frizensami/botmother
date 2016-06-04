import telepot
from telepot.delegate import per_chat_id, create_open
from app.accounts import TelegramAccountManager
from .commands import State
from .questions import AskingQuestions, AnsweringQuestions


class CallbackQueries:
    '''
    This class handles the callback functions.
    The "data" variable will encode the information.
    The "delegator_bot" is to allow notifications on the top of the screen.
    '''
    @classmethod
    def on_answer(cls, bot, delegator_bot, data, query_id):
        # All callback queries will pass through this function and be allocated to
        # a suitable function to handle it based on information in "data"
        callback_type, id1, id2 = data.split('_')
        print callback_type

        # Callback queries for Asking and Answering of questions
        if callback_type == 'AnswerQuestion':
            AnsweringQuestions.callback_answer_question(bot, delegator_bot, data, query_id)
        elif callback_type == 'ConfirmAnswer':
            AnsweringQuestions.callback_confirm_answer(bot, delegator_bot, data, query_id)
        elif callback_type == 'Sent':
            delegator_bot.answerCallbackQuery(query_id, text='Your answer has been sent!')
        elif callback_type == 'Cancelled':
            delegator_bot.answerCallbackQuery(query_id, text='Your answer was cancelled!')

        elif data == 'question_answered':
            CallbackQueries.question_answered(bot, delegator_bot, data, query_id)

    @classmethod
    def question_answered(cls, bot, delegator_bot, data, query_id):
        #
        # BOT EXPIRES WHEN SESSION EXPIRES
        #
        bot.sender.sendMessage("This is data : " + data)
        bot.sender.sendMessage("Question received by callback function!")
        delegator_bot.answerCallbackQuery(query_id, text='Question sent to be voted!')
        # bot = telepot.bot(TOKEN)