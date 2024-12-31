def process_question(question):
    # 定义疑问词列表
    question_words = ['吗', '呢', '吧', '啊', '么', '嘛', '？', '?']
    
    # 去掉所有疑问词和标点
    for word in question_words:
        question = question.replace(word, '')
    
    # 人称转换
    question = replace_pronouns(question)
    return question

def replace_pronouns(text):
    # 临时替换，避免重复替换
    text = text.replace('我', '[TEMP_我]')
    text = text.replace('你', '[TEMP_你]')
    # 进行最终替换
    text = text.replace('[TEMP_我]', '你')
    text = text.replace('[TEMP_你]', '我')
    return text

def chat():
    print("你可以和我聊天了(输入'再见'结束对话)")
    
    # 创建一个对话字典，存储特定问答对
    fixed_responses = {
        "你好": "你好！",
        "在吗": "在的！",
        "再见": "再见，下次再聊！"
    }
    
    while True:
        # 获取用户输入
        user_input = input("你: ").strip()
        
        # 如果用户说再见，结束对话
        if user_input == "再见":
            print("机器人: " + fixed_responses[user_input])
            break
            
        # 先检查是否有固定回复
        if user_input in fixed_responses:
            print("机器人: " + fixed_responses[user_input])
        # 检查是否包含任何疑问词
        elif any(word in user_input for word in ['吗', '呢', '吧', '啊', '么', '嘛', '？', '?']):
            response = process_question(user_input) + "！"
            print("机器人: " + response)
        else:
            # 对一般句子进行人称转换
            response = replace_pronouns(user_input) + "！"
            print("机器人: " + response)

if __name__ == "__main__":
    chat()
