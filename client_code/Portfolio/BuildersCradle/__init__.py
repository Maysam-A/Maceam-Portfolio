from ._anvil_designer import BuildersCradleTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class BuildersCradle(BuildersCradleTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #builds the components
    self.RepeatC2C()
    self.TextC2C()
    
  def RepeatC2C(self, **event_args):
    C2CFlowPanel= FlowPanel(align= "center")
    self.add_component(C2CFlowPanel)
    # Makes the images appear in the main app
    FolioWork= app_tables.showcase.search(Name=q.like('C2C%'))
    AddText= False
    for Name in FolioWork:
      if AddText == False: #This should only occur once, this seperates the hero image from the others. 
        AddText= True
        #the below adds the first image
        img = Image(display_mode= "fill_width", source= Name['PortImg'], vertical_align= "center", role= "faded", horizontal_align= "center", tooltip=Name['AltTxt'])
        C2CFlowPanel.add_component(img, width= 660)
      else:
        img = Image(display_mode= "fill_width", source= Name['PortImg'], vertical_align= "center", role= "faded", horizontal_align= "center", tooltip=Name['AltTxt'])
        C2CFlowPanel.add_component(img, width= 660)
        
  # Makes the text appear in the main app
  def TextC2C(self, **event_args):
    ProjectTextData= app_tables.showcase.get(Name= q.like('C2CHero%'))
    ProjectText= RichText(content= ProjectTextData['Describe'], role= "FadedTxt", align= "left")
    self.add_component(ProjectText)