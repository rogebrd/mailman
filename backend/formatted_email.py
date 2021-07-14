FROM_KEYWORD = "From"
DATE_KEYWORD = "Date"

class FormattedEmail:

  def __init__(self, msg):
    self.msg = msg
    self.formatted_text = ""
    self.formatted_subject = ""
    self.format()

  def format(self):
    lines = self.msg.text.splitlines()    
    self.format_text(lines)
    self.format_subject()
    self.set_foldername(lines)


  def format_text(self, lines):
    if not lines:
      return
    keyword_line_indices = [i for i in range(len(lines)) if FROM_KEYWORD in lines[i]]
    cut_index = keyword_line_indices[0] if keyword_line_indices else 0
    formatted_text = "\n".join(lines[cut_index:])
    self.formatted_text = formatted_text
  
  def set_foldername(self, lines):
    if not lines:
      return
    keyword_line_indices = [i for i in range(len(lines)) if DATE_KEYWORD in lines[i]]
    date_string = ""
    if keyword_line_indices:
      cut_index = lines[keyword_line_indices[0]].find(DATE_KEYWORD) + len(DATE_KEYWORD) + 2
      date_string = lines[keyword_line_indices[0]][cut_index:]
    self.foldername = self.formatted_subject + "_" + date_string

  
  def format_subject(self):
    if not self.msg.subject:
      return
    cut_index = self.msg.subject.find(":")
    if cut_index == -1 or cut_index == len(self.msg.subject) - 1:
      self.formatted_subject = self.msg.subject[:]
    else:
      if self.msg.subject[cut_index+1] == " ":
        cut_index += 1
      self.formatted_subject = self.msg.subject[cut_index+1:]