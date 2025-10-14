'''

'''


class control_panel:
    
    def __init__(self):
        self.groups={}

    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created !!')
        else:
            print('your group name is duplicated')
        
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            # groups['living_room'] -->[]
            print(f'your device is added to {group_name}')
        else:
            print(f'your {group_name} is not exist')
        
        
        
        
    def create_device(self,group_name,device_type,device_name):
        if group_name in self.groups:
            location='home'
            new_device=Device(location,group_name,device_type,device_name)
            self.groups[group_name].append(new_device)
            print(f'Device {device_name} successfully created in group {group_name} DONE!!')
        else:
            print(f"Group {group_name} doesn't exist.Please create it first")
            
#mr: این دو👆🏻 کد پرینت اضافه شد

              
    def create_multiple_device(self,group_name,device_type,device_number):
        if group_name in self.groups:
            for i in range(1,device_number+1):
                dv_name=f'{device_type}_{i}'
                self.create_device(group_name,device_type,dv_name)
            print(f'All {device_number} {device_type} devices is added to {group_name} DONE!!')
        else:
            print(f'Group {group_name} doesnt exist. Please create it first')
            
  #mr: این دو👆🏻 کد پرینت اضافه شد

            
    def get_devices(self,group_name):
        devices=self.groups[group_name]
        return devices
        
    def trun_on_in_group(self,group_name):
        if group_name in self.groups:
            devices=self.get_devices(group_name)
            for device in devices:
                device.turn_on()
            print(f'All devices in group {group_name} turned ON')
        else:
            print(f'Group {group_name} doesn't exist. Please create it first.') 
   #mr: این دو👆🏻 کد پرینت اضافه شد
        
