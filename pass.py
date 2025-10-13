
    def turn_off_in_group(self, group_name):
        if group_name in self.groups:
            devices=self.get_devices(group_name)
            for device in devices:
                device.turn_off()
            print(f'All devices in group {group_name} turned OFF')
        else:
            print(f'Group {group_name} doesn't exist. Please create it first.')

    def turn_on_all(self):
        for group_name, devices in self.groups.items():
            for device in devices:
                device.turn_on()
        if device=True
            print('All devices in all groups turned ON')
        else:
            print('No groups found')

    def turn_off_all(self):
        for group_name, devices in self.groups.items():
            for device in devices:
                device.turn_off()
        if device=True
            print('All devices turned OFF')
        else:
            print('No groups found')

    def get_status_in_group(self,group_name):
        if group_name in self.groups:
            devices=self.groups[group_name]
            if not devices:
                print(f'No devices found in group {group_name}')
                return[]
            result=[]
            for device in devices:
               if device.get_status():
                   st='on'
               else:
                   st='off'
                print(f'device {device.device_name} is {st}')
                result.append((device.device_name, st))
            print('Status checked successfully')
            return result
        else:
            print(f'Group {group_name} doesn't exist. Please create it first')
            return[]

    def get_status_in_device_type(self,dvice_type):
        result=[]
        for group_name, devices in self.groups.items():
            for device in devices:
                if device.device_type==device_type:
                    if device.get_status():
                        st='on'
                    else:
                        st='off'
                    print(f'device {device.device_name} in group {group_name} is {st}')
                    result.append((group_name, device.device_name, st))
                    found_any=True
        if found_any:
            print('Status checked successfully')
            return result
        else:
            print(f'No device found for type {dvice_type}')
            return[]


    def create_sensor(self):
        if group_name in self.groups:
            location=home
            new_sensor=Device(location,group_name,sensor_type,sensor_name)
            self.groups[group_name].appnd(new_sensor)
            print(f'Sensor {sensor_name} created in group {group_name} DONE!!')
            return new_sensor
        else:
            print(f'Group {group_name} doesn't exist. Please create it first')
            return None
    
    def create_multiple_sensor(self):
        if group_name in self.groups:
            for i in range(1,sensor_number+1):
                name=f'{sensor_type}_{i}'
                s=self.create_sensor(group_name, sensor_type, name)
            if created:
                print(f'All {sensor_number} {sensor_type} sensors are added to {group_name} DONE!!')
            else:
                print(f'No sensors were created in {group_name}')
            return created
        else:
            print(f'Group {group_name} doesnt exist. Please create it first')
            return []
