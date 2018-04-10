
# 状态定义
states=['wait', 'pass', 'not pass']

# 定义状态转移
# The trigger argument defines the name of the new triggering method
transitions = [
    {'trigger': 'review', 'source': 'wait', 'dest': 'pass' },
    {'trigger': 'review_not_pass', 'source': 'wait', 'dest': 'not pass'},
    {'trigger': 'back_wait', 'source': 'initial', 'dest': 'wait'}]


