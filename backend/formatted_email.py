import calendar 

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
    basename = self.get_basename(lines)
    if basename:
      self.set_pathname(lines, basename)
    else:
      self.set_pathname(lines)

  def format_text(self, lines):
    if not lines:
      return
    keyword_line_indices = [i for i in range(len(lines)) if FROM_KEYWORD in lines[i]]
    cut_index = keyword_line_indices[0] if keyword_line_indices else 0
    formatted_text = "\n".join(lines[cut_index:])
    self.formatted_text = formatted_text
  
  def get_basename(self, lines):
    for line in lines:
      if "folder" in line.lower():
        words = line.split(" ")
        for i, word in enumerate(words):
          if "folder" in word.lower() and i != len(words) - 1:
            basename = words[i+1]
            basename = basename[:-1] if basename[-1] == "/" else basename
            return f'/{basename}'
    return None

  def set_pathname(self, lines, basepath="/Mailman"):
    if not lines:
      self.pathname = self.formatted_subject
      self.filename = self.formatted_subject
    keyword_line_indices = [i for i in range(len(lines)) if DATE_KEYWORD in lines[i]]
    date_string = ""
    if not keyword_line_indices:
      print("no date")
      self.pathname = self.formatted_subject
      self.filename = self.formatted_subject
      return
    line_index = keyword_line_indices[0]
    words = lines[line_index].split(" ")
    year_index = [i for i in range(len(words)) if words[i].isnumeric()][0]
    month_map = {month: index for index, month in enumerate(calendar.month_name) if month}
    if words[year_index-2] not in month_map:
      month_map = {month: index for index, month in enumerate(calendar.month_abbr) if month}
    month = str(month_map[words[year_index-2]])
    if len(month) == 1:
      month = "0" + month
    day = words[year_index-1]
    if not day[-1].isnumeric():
      day = day[:-1]
    year = words[year_index]
    filename = f'{month}-{day}-{year} - {self.formatted_subject}'
    if not self.msg.attachments:
      self.pathname = f'{basepath}/'
    else:
      self.pathname = f'{basepath}/{filename}/'
    self.filename = f'{filename}.txt'

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
