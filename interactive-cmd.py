from cmd2 import cmd


class InvestigationAgent(cmd.Cmd):

  prompt = "Command ###:"
  FRIENDS = [ 'Adam', 'Bob' ]

  def do_greet(self, line):
    "Greet the person"
    print "hello"

  def do_exit(self, line):
    "Exiting the application"
    return True

  def complete_greet(self, text, line, befidx, endidx):
    if not text:
       completions = self.FRIENDS[:]
    else:
       completions = [ f
                       for f in self.FRIENDS
                       if f.startwith(text)
                       ]
    return completions

if __name__ == '__main__':
    InvestigationAgent().cmdloop()
