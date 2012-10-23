import time
import android
droid = android.Android()

class Params():
    def __init__(self):
        params = droid.getIntent().result[u'extras']
        for key in params.keys():
            if key.startswith('%'):
                exec "self." + key.lstrip('%') + '="' + params[key] + '"'

class Task():
    SET_VARIABLE = 547
    def new_task(self):
        self.action_cnt = 0
        self.extras = {'version_number': '1.0', 'task_name': 'task' + str(time.time()), 'task_priority': 9 }
    def set_var(self, varname, value):
        self.action_cnt += 1
        self.extras['action' + str(self.action_cnt)] = {'action': self.SET_VARIABLE, 'arg:1': varname, 'arg:2': value, 'arg:3': False, 'arg:4': False, 'arg:5': False}
    def run_task(self):
        taskIntent = droid.makeIntent('net.dinglisch.android.tasker.ACTION_TASK', None, None, self.extras).result
        droid.sendBroadcastIntent(taskIntent)
    def set_var_now(self, varname, value):
        self.new_task()
        self.set_var(varname, value)
        self.run_task()

class Stderr():
    def __init__(self, progname):
        self.errmsg = ''
        self.progname = progname
    def write(self,s):
        if self.errmsg == '':
            self.err = Task()
            self.err.set_var_now("%SCRIPT", self.progname)
        self.errmsg += s
        self.err.set_var_now("%STDERR", self.errmsg)
