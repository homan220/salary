class ViewGenerator():
    
    def __init__(self,table,opration_buttons=False,select_checkbox=False,add_url='home'):
        self.table=table
        self.add_url=add_url
    # get all fields names of table 
    def get_filed_names(self):
        filed_names=list()
        for f in self.table._meta.get_fields():
            if hasattr(f,'verbose_name'):
                filed_names.append(f.name)
        return filed_names
        
    # get all fields labels of table
    def get_field_labels(self):
        filed_labels=list()
        for f in self.table._meta.get_fields():
            if hasattr(f,'verbose_name'):
                filed_labels.append(f.verbose_name)
        return filed_labels

    # create context for html template
    def get_context_template(self):
        context={
        'objects':self.table.objects.all(),
        'titles': self.get_field_labels(),
        'field_names':self.get_filed_names(),
        'add_url_name':self.add_url,
        'opration_buttons':True,
        'select_checkbox':True,
        }

        return context
