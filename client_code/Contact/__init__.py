from ._anvil_designer import ContactTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Contact(ContactTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  @anvil.email.handle_message(require_dkim=True)
  def ButtonSubmit_click(self, **event_args):
    """This method is called when the button is clicked"""
    Name = self.NameTxt.text
    Email = self.EmailTxt.text
    Subject = self.SubjectTxt.text
    Message = self.MsgTxt.text
    if Name and Email and Subject and Message and msg.dkim.domains is not None:
      anvil.server.call('add_contact_info', Name, Email, Subject, Message)
      alert("Thanks for getting in touch!")
      self.NameTxt.text = ""
      self.EmailTxt.text = ""
      self.SubjectTxt.text = ""
      self.MsgTxt.text = ""
    else:
      alert("Please fill out the entire form before submitting.")
