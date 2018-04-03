from pykit import proc


returncode, out, err = proc.command('ls', '-al', cwd='/home/cheng')

'''
for i in out.split("\n"):
    print i
    print
print returncode
print err
'''

returncode, out, err = proc.shell_script('ls -al', cwd='/home/cheng')
'''
print out
'''

proc.start_process('csv_to_json.py', '/home/cheng/test_json/', 'p'='a')
