try:
        from GenericSimulationLibrary import SimulationInterface
except:
        from simulation_interface import SimulationInterface

inputs = {
         "x_min":0, 
         "x_max":10, 
         "N_points":30,
         "m":1.5,
         "b":1,
         "filename":"test_1.sim"
        }
data = {
         "x":[0,1,2,3], 
         "y":[0,1,2,3], 
         "plot_options":None
       }
SI = SimulationInterface()
SI.plot(display=True)
SI.status()
SI.new(inputs, data)
SI.plot(display=True)
SI.status()
SI.simulate()
SI.plot(display=True)
SI.status()
SI.export_xlsx("test_3.xlsx")
SI.plot(display=True)
SI.save()