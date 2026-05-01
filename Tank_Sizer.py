import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import pandas as pd

PI = np.pi

def safe_get(var, default=0.0):
    try:
        return var.get()
    except (tk.TclError, ValueError, TypeError):
        return default


def safe_int(var, default=0):
    try:
        return int(var.get())
    except (tk.TclError, ValueError, TypeError):
        return default


def click_me():
    messagebox.showinfo("Tank Sizer", "Button clicked")

def export_to_excel():
    try:
        if Export_units.get() == "in":
            Fuel_Tank_Parameters = {'Parameter':['Tank_Outer_Diameter', 'Tank_Inner_Diameter', 'Tank_Shell_Height', 'Outlet_Cap_Wall_Thickness', 
                            'Outlet_Cap_Knuckle_Radius','Outlet_Cap_Crown_Radius', 'Outlet_Cap_Skirt_Length'],
                                'Value':[fuel_tank_outer_diameter_in.get(), fuel_tank_inner_diameter_in.get(), fuel_internal_height_in.get(), fuel_cap_thickness_in.get(), fuel_cap_knuckle_radius_in.get(), 
                                fuel_cap_crown_radius_in.get(), fuel_cap_skirt_in.get()], 
                                'Unit':['in', 'in', 'in', 'in', 'in', 'in', 'in']
                                    }
            Oxidiser_Tank_Parameters = {
                                'Parameter':['Tank_Outer_Diameter', 'Tank_Inner_Diameter', 'Tank_Shell_Height', 'Outlet_Cap_Wall_Thickness', 
                            'Outlet_Cap_Knuckle_Radius','Outlet_Cap_Crown_Radius', 'Outlet_Cap_Skirt_Length'],
                                'Value':[oxidiser_tank_outer_diameter_in.get(), oxidiser_tank_inner_diameter_in.get(), oxidiser_internal_height_in.get(), oxidiser_cap_thickness_in.get(), oxidiser_cap_knuckle_radius_in.get(), 
                                oxidiser_cap_crown_radius_in.get(), oxidiser_cap_skirt_in.get()], 
                                'Unit':['in', 'in', 'in', 'in', 'in', 'in', 'in']
                                    }
        elif Export_units.get() == "mm":
            Fuel_Tank_Parameters = {
                                'Parameter':['Tank_Outer_Diameter', 'Tank_Inner_Diameter', 'Tank_Shell_Height', 'Outlet_Cap_Wall_Thickness', 
                            'Outlet_Cap_Knuckle_Radius','Outlet_Cap_Crown_Radius', 'Outlet_Cap_Skirt_Length'],
                                'Value':[fuel_tank_outer_diameter_mm.get(), fuel_tank_inner_diameter_mm.get(), fuel_internal_height_mm.get(), fuel_cap_thickness_mm.get(), 
                                fuel_cap_knuckle_radius_mm.get(), fuel_cap_crown_radius_mm.get(), fuel_cap_skirt_mm.get()], 
                                'Unit':['mm', 'mm', 'mm', 'mm', 'mm', 'mm', 'mm']
                                    }
            Oxidiser_Tank_Parameters = {
                                'Parameter':['Tank_Outer_Diameter', 'Tank_Inner_Diameter', 'Tank_Shell_Height', 'Outlet_Cap_Wall_Thickness', 
                            'Outlet_Cap_Knuckle_Radius','Outlet_Cap_Crown_Radius', 'Outlet_Cap_Skirt_Length'],
                                'Value':[oxidiser_tank_outer_diameter_mm.get(), oxidiser_tank_inner_diameter_mm.get(), oxidiser_internal_height_mm.get(), oxidiser_cap_thickness_mm.get(), 
                                oxidiser_cap_knuckle_radius_mm.get(), oxidiser_cap_crown_radius_mm.get(), oxidiser_cap_skirt_mm.get()], 
                                'Unit':['mm', 'mm', 'mm', 'mm', 'mm', 'mm', 'mm']
                                    }
        Fuel_Tank_Parameters_df = pd.DataFrame(Fuel_Tank_Parameters)
        Oxidiser_Tank_Parameters_df = pd.DataFrame(Oxidiser_Tank_Parameters)
        Fuel_Tank_Parameters_df.to_excel(r"C:\Users\jackr\OneDrive\ERPL\Flight Vehicle\CAD\Fuel_Tank_Parameters.xlsx", sheet_name="Fuel Tank Parameters", index=False)
        Oxidiser_Tank_Parameters_df.to_excel(r"C:\Users\jackr\OneDrive\ERPL\Flight Vehicle\CAD\Oxidiser_Tank_Parameters.xlsx", sheet_name="Oxidiser Tank Parameters", index=False)

        print("=== UPDATE COMPLETE ===")
        messagebox.showinfo("Tank Sizer", "Export to Excel successful!")
    except Exception as e:
        print(f"=== ERROR OCCURRED ===")
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
def update_all(event=None):
    try:
        ##### Vehicle Diameter #####
        if Vehicle_Diameter_units.get() == "in":
            vehicle_diameter_in.set(vehicle_diameter_INPUT.get())
            vehicle_diameter_mm.set(vehicle_diameter_in.get() * in_mm)
            vehicle_diameter_m.set(vehicle_diameter_in.get() * in_m)
        elif Vehicle_Diameter_units.get() == "mm":
            vehicle_diameter_mm.set(vehicle_diameter_INPUT.get())
            vehicle_diameter_in.set(vehicle_diameter_mm.get() * mm_in)
            vehicle_diameter_m.set(vehicle_diameter_mm.get() * 1e-3)

        ##### Tank Outer Diameter Units #####
        fuel_tank_outer_diameter_in.set(vehicle_diameter_in.get())
        fuel_tank_outer_diameter_mm.set(vehicle_diameter_mm.get())
        fuel_tank_outer_diameter_m.set(vehicle_diameter_m.get())
        oxidiser_tank_outer_diameter_in.set(vehicle_diameter_in.get())
        oxidiser_tank_outer_diameter_mm.set(vehicle_diameter_mm.get())
        oxidiser_tank_outer_diameter_m.set(vehicle_diameter_m.get())

        ## MEOP Conversions ##
        if meop_units.get() == "Psi":
            fuel_meop_psi.set(fuel_meop_INPUT.get())
            fuel_meop_Pa.set(fuel_meop_psi.get() * psi_pa)
            oxidiser_meop_psi.set(oxidiser_meop_INPUT.get())
            oxidiser_meop_Pa.set(oxidiser_meop_psi.get() * psi_pa)
        elif meop_units.get() == "Pa":
            fuel_meop_Pa.set(fuel_meop_INPUT.get())
            fuel_meop_psi.set(fuel_meop_Pa.get() * pa_psi)
            oxidiser_meop_Pa.set(oxidiser_meop_INPUT.get())
            oxidiser_meop_psi.set(oxidiser_meop_Pa.get() * pa_psi)

        ## Allowable Stress Conversions ##
        if stress_units.get() == "MPa":
            allowable_stress_MPa.set(allowable_stress_INPUT.get())
            allowable_stress_Pa.set(allowable_stress_MPa.get() * MPa_Pa)
            allowable_stress_psi.set(allowable_stress_MPa.get() * MPa_psi)
        elif stress_units.get() == "Psi":
            allowable_stress_psi.set(allowable_stress_INPUT.get())
            allowable_stress_Pa.set(allowable_stress_psi.get() * psi_pa)
            allowable_stress_MPa.set(allowable_stress_psi.get() * psi_MPa)

        ##### Tank Inner Diameter Units #####
        fuel_tank_inner_diameter_mm.set(fuel_tank_outer_diameter_mm.get()*(allowable_stress_Pa.get()*weld_efficiency.get()-0.6*(1.25*fuel_meop_Pa.get()))/(allowable_stress_Pa.get()*weld_efficiency.get()+0.4*(1.25*fuel_meop_Pa.get())))
        fuel_tank_inner_diameter_in.set(fuel_tank_inner_diameter_mm.get() * mm_in)
        fuel_tank_inner_diameter_m.set(fuel_tank_inner_diameter_mm.get() * 1e-3)
        oxidiser_tank_inner_diameter_mm.set(oxidiser_tank_outer_diameter_mm.get()*(allowable_stress_Pa.get()*weld_efficiency.get()-0.6*(1.25*oxidiser_meop_Pa.get()))/(allowable_stress_Pa.get()*weld_efficiency.get()+0.4*(1.25*oxidiser_meop_Pa.get())))
        oxidiser_tank_inner_diameter_in.set(oxidiser_tank_inner_diameter_mm.get() * mm_in)
        oxidiser_tank_inner_diameter_m.set(oxidiser_tank_inner_diameter_mm.get() * 1e-3)

        ##### Tank Wall Thickness Units #####

        fuel_wall_thickness_in.set((fuel_tank_outer_diameter_in.get() - fuel_tank_inner_diameter_in.get())/2)
        oxidiser_wall_thickness_in.set((oxidiser_tank_outer_diameter_in.get() - oxidiser_tank_inner_diameter_in.get())/2)   
        fuel_wall_thickness_mm.set(fuel_wall_thickness_in.get() * in_mm)
        fuel_wall_thickness_m.set(fuel_wall_thickness_mm.get() * 1e-3)
        oxidiser_wall_thickness_mm.set(oxidiser_wall_thickness_in.get() * in_mm)
        oxidiser_wall_thickness_m.set(oxidiser_wall_thickness_mm.get() * 1e-3)

        ###### Propellant Mass, Volume, and Internal Height Calcs ######
        ## Density Conversions ##
        if propellant_density_units.get() == "kg/m³":
            fuel_density_kgm3.set(safe_get(fuel_density_INPUT, 0.0))
            fuel_density_lbin3.set(fuel_density_kgm3.get() * kgm3_lbmin3)
            oxidiser_density_kgm3.set(safe_get(oxidiser_density_INPUT, 0.0))
            oxidiser_density_lbin3.set(oxidiser_density_kgm3.get() * kgm3_lbmin3)
        elif propellant_density_units.get() == "lb/in³":
            fuel_density_lbin3.set(safe_get(fuel_density_INPUT, 0.0))
            fuel_density_kgm3.set(fuel_density_lbin3.get() * lbmin3_kgm3)
            oxidiser_density_lbin3.set(safe_get(oxidiser_density_INPUT, 0.0))
            oxidiser_density_kgm3.set(oxidiser_density_lbin3.get() * lbmin3_kgm3)

        ## Mass Flow Rate Conversions ##
        if MassFlowRate_units.get() == "kg/s":
            fuel_mass_flow_kgs.set(fuel_mass_flow_INPUT.get())
            fuel_mass_flow_lbs.set(fuel_mass_flow_kgs.get() * kgs_lbm)
            oxidiser_mass_flow_kgs.set(oxidiser_mass_flow_INPUT.get())
            oxidiser_mass_flow_lbs.set(oxidiser_mass_flow_kgs.get() * kgs_lbm)
        elif MassFlowRate_units.get() == "lb/s":
            fuel_mass_flow_lbs.set(fuel_mass_flow_INPUT.get())
            fuel_mass_flow_kgs.set(fuel_mass_flow_lbs.get() * lb_kg)
            oxidiser_mass_flow_lbs.set(oxidiser_mass_flow_INPUT.get())
            oxidiser_mass_flow_kgs.set(oxidiser_mass_flow_lbs.get() * lb_kg)

        ## Mass ##
        fuel_propellant_mass_kg.set(fuel_mass_flow_kgs.get() * run_time.get())
        oxidiser_propellant_mass_kg.set(oxidiser_mass_flow_kgs.get() * run_time.get())
        fuel_propellant_mass_lb.set(fuel_mass_flow_lbs.get() * run_time.get())
        oxidiser_propellant_mass_lb.set(oxidiser_mass_flow_lbs.get() * run_time.get())

        ## Volume No Ullage ##
        fuel_propellant_volume_L.set(fuel_propellant_mass_kg.get() / fuel_density_kgm3.get() * 1000)
        oxidiser_propellant_volume_L.set(oxidiser_propellant_mass_kg.get() / oxidiser_density_kgm3.get() * 1000)
        fuel_propellant_volume_in3.set(fuel_propellant_mass_lb.get() / fuel_density_lbin3.get())
        oxidiser_propellant_volume_in3.set(oxidiser_propellant_mass_lb.get() / oxidiser_density_lbin3.get())

        ## Required Volume W/Ullage ##
        fuel_required_volume_L.set(fuel_propellant_volume_L.get() * (1 + fuel_ullage.get()/100))
        oxidiser_required_volume_L.set(oxidiser_propellant_volume_L.get() * (1 + oxidiser_ullage.get()/100))
        fuel_required_volume_in3.set(fuel_propellant_volume_in3.get() * (1 + fuel_ullage.get()/100))
        oxidiser_required_volume_in3.set(oxidiser_propellant_volume_in3.get() * (1 + oxidiser_ullage.get()/100))

        ##### Cap Calculations ######
        ## Calculate cap height first (needed for volume calculation) ##
        fuel_cap_height_in.set(fuel_tank_inner_diameter_in.get() / 4)
        fuel_cap_height_mm.set(fuel_cap_height_in.get() * in_mm)
        fuel_cap_height_m.set(fuel_cap_height_in.get() * in_m)
        oxidiser_cap_height_in.set(oxidiser_tank_inner_diameter_in.get() / 4)
        oxidiser_cap_height_mm.set(oxidiser_cap_height_in.get() * in_mm)
        oxidiser_cap_height_m.set(oxidiser_cap_height_in.get() * in_m)

        ## Convert cap skirt from inches to millimeters ##
        if cap_skirt_units.get() == "in":
            fuel_cap_skirt_in.set(fuel_cap_skirt_INPUT.get())
            fuel_cap_skirt_mm.set(fuel_cap_skirt_in.get() * in_mm)
            fuel_cap_skirt_m.set(fuel_cap_skirt_in.get() * in_m)
            oxidiser_cap_skirt_in.set(oxidiser_cap_skirt_INPUT.get())
            oxidiser_cap_skirt_mm.set(oxidiser_cap_skirt_in.get() * in_mm)
            oxidiser_cap_skirt_m.set(oxidiser_cap_skirt_in.get() * in_m)
        elif cap_skirt_units.get() == "mm":
            fuel_cap_skirt_mm.set(fuel_cap_skirt_INPUT.get())
            fuel_cap_skirt_in.set(fuel_cap_skirt_mm.get() * mm_in)
            fuel_cap_skirt_m.set(fuel_cap_skirt_mm.get() * 1e-3)
            oxidiser_cap_skirt_mm.set(oxidiser_cap_skirt_INPUT.get())
            oxidiser_cap_skirt_in.set(oxidiser_cap_skirt_mm.get() * mm_in)
            oxidiser_cap_skirt_m.set(oxidiser_cap_skirt_mm.get() * 1e-3)

        ## Calculate cap thickness ##
        fuel_cap_thickness_m.set((fuel_meop_Pa.get()*fuel_tank_inner_diameter_m.get())/(2*allowable_stress_Pa.get()*weld_efficiency.get() - 0.2*fuel_meop_Pa.get()))
        fuel_cap_thickness_mm.set(fuel_cap_thickness_m.get() * 1000)
        fuel_cap_thickness_in.set(fuel_cap_thickness_mm.get() * mm_in)
        oxidiser_cap_thickness_m.set((oxidiser_meop_Pa.get()*oxidiser_tank_inner_diameter_m.get())/(2*allowable_stress_Pa.get()*weld_efficiency.get() - 0.2*oxidiser_meop_Pa.get()))
        oxidiser_cap_thickness_mm.set(oxidiser_cap_thickness_m.get() * 1000)
        oxidiser_cap_thickness_in.set(oxidiser_cap_thickness_mm.get() * mm_in)

        ## Calculate cap knuckle radius ##
        fuel_cap_knuckle_radius_in.set((fuel_tank_outer_diameter_in.get()-2*fuel_cap_thickness_in.get()) * 0.17)
        fuel_cap_knuckle_radius_mm.set(fuel_cap_knuckle_radius_in.get() * in_mm)
        fuel_cap_knuckle_radius_m.set(fuel_cap_knuckle_radius_in.get() * in_m)
        oxidiser_cap_knuckle_radius_in.set((oxidiser_tank_outer_diameter_in.get() - 2*oxidiser_cap_thickness_in.get()) * 0.17)
        oxidiser_cap_knuckle_radius_mm.set(oxidiser_cap_knuckle_radius_in.get() * in_mm)
        oxidiser_cap_knuckle_radius_m.set(oxidiser_cap_knuckle_radius_in.get() * in_m)

        ## Calculate cap crown radius ##
        fuel_cap_crown_radius_in.set((fuel_tank_outer_diameter_in.get()-2*fuel_cap_thickness_in.get()) * 0.9)
        fuel_cap_crown_radius_mm.set(fuel_cap_crown_radius_in.get() * in_mm)
        fuel_cap_crown_radius_m.set(fuel_cap_crown_radius_in.get() * in_m)
        oxidiser_cap_crown_radius_in.set((oxidiser_tank_outer_diameter_in.get() - 2*oxidiser_cap_thickness_in.get()) * 0.9)
        oxidiser_cap_crown_radius_mm.set(oxidiser_cap_crown_radius_in.get() * in_mm)
        oxidiser_cap_crown_radius_m.set(oxidiser_cap_crown_radius_in.get() * in_m)

        ## Calculate cap skirt lengths ##
        if cap_skirt_units.get() == "in":
            fuel_cap_skirt_in.set(fuel_cap_skirt_INPUT.get())
            fuel_cap_skirt_mm.set(fuel_cap_skirt_in.get() * in_mm)
            oxidiser_cap_skirt_in.set(oxidiser_cap_skirt_INPUT.get())
            oxidiser_cap_skirt_mm.set(oxidiser_cap_skirt_in.get() * in_mm)
        elif cap_skirt_units.get() == "mm":
            fuel_cap_skirt_mm.set(fuel_cap_skirt_INPUT.get())
            fuel_cap_skirt_in.set(fuel_cap_skirt_mm.get() * mm_in)
            oxidiser_cap_skirt_mm.set(oxidiser_cap_skirt_INPUT.get())
            oxidiser_cap_skirt_in.set(oxidiser_cap_skirt_mm.get() * mm_in)

        ## Calculate cap volume ##
        fuel_cap_volume_m3.set((PI * fuel_tank_inner_diameter_m.get()**3) / 24 + ((PI * (fuel_tank_inner_diameter_m.get()**2)) / 4) * fuel_cap_skirt_m.get())
        fuel_cap_volume_L.set(fuel_cap_volume_m3.get() * m3_L)
        fuel_cap_volume_in3.set((fuel_cap_volume_m3.get() * m3_L) * L_in3)
          
        oxidiser_cap_volume_m3.set((PI * oxidiser_tank_inner_diameter_m.get()**3) / 24 + ((PI * (oxidiser_tank_inner_diameter_m.get()**2)) / 4) * oxidiser_cap_skirt_m.get())
        oxidiser_cap_volume_L.set(oxidiser_cap_volume_m3.get() * m3_L)
        oxidiser_cap_volume_in3.set((oxidiser_cap_volume_m3.get() * m3_L) * L_in3)

        ##### Shell Volume Calculations ######
        fuel_shell_volume_L.set(fuel_required_volume_L.get() - 2*fuel_cap_volume_L.get())
        fuel_shell_volume_m3.set(fuel_shell_volume_L.get() * L_m3)
        fuel_shell_volume_in3.set(fuel_shell_volume_L.get() * L_in3)
        
        oxidiser_shell_volume_L.set(oxidiser_required_volume_L.get() - 2*oxidiser_cap_volume_L.get())
        oxidiser_shell_volume_m3.set(oxidiser_shell_volume_L.get() * L_m3)
        oxidiser_shell_volume_in3.set(oxidiser_shell_volume_L.get() * L_in3)
        
        ##### Shell Height Calculations ######
        fuel_internal_height_m.set((fuel_shell_volume_m3.get()) / ((PI * (fuel_tank_inner_diameter_m.get()**2)) / 4))
        fuel_internal_height_mm.set(fuel_internal_height_m.get() * 1000)
        fuel_internal_height_in.set(fuel_internal_height_m.get() * m_in)
        
        oxidiser_internal_height_m.set((oxidiser_shell_volume_m3.get()) / ((PI * (oxidiser_tank_inner_diameter_m.get()**2)) / 4))
        oxidiser_internal_height_mm.set(oxidiser_internal_height_m.get() * 1000)
        oxidiser_internal_height_in.set(oxidiser_internal_height_m.get() * m_in)

        ##### Pressure Calculations #####
        fuel_mawp_circ_Pa.set((allowable_stress_Pa.get()*weld_efficiency.get()*fuel_wall_thickness_m.get())/((fuel_tank_inner_diameter_m.get()/2)+(0.6*fuel_wall_thickness_m.get())))
        oxidiser_mawp_circ_Pa.set((allowable_stress_Pa.get()*weld_efficiency.get()*oxidiser_wall_thickness_m.get())/((oxidiser_tank_inner_diameter_m.get()/2)+(0.6*oxidiser_wall_thickness_m.get())))
        fuel_mawp_circ_psi.set(fuel_mawp_circ_Pa.get() * pa_psi)
        oxidiser_mawp_circ_psi.set(oxidiser_mawp_circ_Pa.get() * pa_psi)
        
        fuel_mawp_long_Pa.set((2*allowable_stress_Pa.get()*weld_efficiency.get()*fuel_wall_thickness_m.get())/((fuel_tank_inner_diameter_m.get()/2)-(0.4*fuel_wall_thickness_m.get())))
        fuel_mawp_long_psi.set(fuel_mawp_long_Pa.get() * pa_psi)
        oxidiser_mawp_long_Pa.set((2*allowable_stress_Pa.get()*weld_efficiency.get()*oxidiser_wall_thickness_m.get())/((oxidiser_tank_inner_diameter_m.get()/2)-(0.4*oxidiser_wall_thickness_m.get())))
        oxidiser_mawp_long_psi.set(oxidiser_mawp_long_Pa.get() * pa_psi)

        fuel_hydro_pressure_Pa.set(fuel_mawp_circ_Pa.get() * 1.5)
        fuel_hydro_pressure_psi.set(fuel_hydro_pressure_Pa.get() * pa_psi)
        oxidiser_hydro_pressure_Pa.set(oxidiser_mawp_circ_Pa.get() * 1.5)
        oxidiser_hydro_pressure_psi.set(oxidiser_hydro_pressure_Pa.get() * pa_psi)

        fuel_relief_pressure_Pa.set(fuel_mawp_circ_Pa.get() * 1.25)
        fuel_relief_pressure_psi.set(fuel_relief_pressure_Pa.get() * pa_psi)
        oxidiser_relief_pressure_Pa.set(oxidiser_mawp_circ_Pa.get() * 1.25)
        oxidiser_relief_pressure_psi.set(oxidiser_relief_pressure_Pa.get() * pa_psi)

    except Exception as e:
        print(f"=== ERROR OCCURRED ===")
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def create_inlet_port_rows(frame, port_type, num_ports):
    """
    Create dynamic rows for inlet port sizes appearing under the inlet port number input.
    Also repositions outlet port section below inlet ports.
    
    Args:
        frame: The parent frame to add rows to
        port_type: 'fuel' or 'oxidiser'
        num_ports: Number of ports to create
    """
    global fuel_inlet_port_entries, fuel_inlet_port_labels, oxidiser_inlet_port_entries, oxidiser_inlet_port_labels
    
    # Clear existing entries and labels
    if port_type == 'fuel':
        for entry in fuel_inlet_port_entries:
            entry.grid_forget()
        for label in fuel_inlet_port_labels:
            label.grid_forget()
        fuel_inlet_port_entries = []
        fuel_inlet_port_labels = []
        entries_list = fuel_inlet_port_entries
        labels_list = fuel_inlet_port_labels
    else:
        for entry in oxidiser_inlet_port_entries:
            entry.grid_forget()
        for label in oxidiser_inlet_port_labels:
            label.grid_forget()
        oxidiser_inlet_port_entries = []
        oxidiser_inlet_port_labels = []
        entries_list = oxidiser_inlet_port_entries
        labels_list = oxidiser_inlet_port_labels
    
    # Create new entries
    try:
        num = int(num_ports)
        col = 1 if port_type == 'fuel' else 3
        start_row = 3  # Start right after inlet port number input (row 2)
        
        for i in range(num):
            port_label = ttk.Label(frame, text=f"Port {i+1} Size (in):")
            port_label.grid(row=start_row + i, column=col-1, padx=5, pady=3, sticky=tk.E)
            labels_list.append(port_label)
            
            port_entry = tk.Entry(frame, width=10, bg='lightblue', fg='black')
            port_entry.grid(row=start_row + i, column=col, padx=5, pady=3)
            entries_list.append(port_entry)
        
        # Reposition outlet port section based on number of inlet ports
        outlet_start_row = start_row + num + 1
        Cap_Outlet_Ports.grid(row=outlet_start_row, column=0, padx=5, pady=5, sticky=tk.E)
        Fuel_Cap_Outlet_Ports_entry.grid(row=outlet_start_row, column=1, padx=5, pady=5)
        Oxidiser_Cap_Outlet_Ports_entry.grid(row=outlet_start_row, column=3, padx=5, pady=5)
        
        # Update outlet port rows positioning
        update_outlet_port_rows_position(frame, outlet_start_row + 1)
        
    except (ValueError, TypeError):
        pass

def update_outlet_port_rows_position(frame, start_row):
    """Update the position of outlet port entry rows"""
    global fuel_outlet_port_entries, fuel_outlet_port_labels, oxidiser_outlet_port_entries, oxidiser_outlet_port_labels
    
    # Reposition fuel outlet entries
    for i, (label, entry) in enumerate(zip(fuel_outlet_port_labels, fuel_outlet_port_entries)):
        label.grid(row=start_row + i, column=0, padx=5, pady=3, sticky=tk.E)
        entry.grid(row=start_row + i, column=1, padx=5, pady=3)
    
    # Reposition oxidiser outlet entries
    for i, (label, entry) in enumerate(zip(oxidiser_outlet_port_labels, oxidiser_outlet_port_entries)):
        label.grid(row=start_row + i, column=2, padx=5, pady=3, sticky=tk.E)
        entry.grid(row=start_row + i, column=3, padx=5, pady=3)

def create_outlet_port_rows(frame, port_type, num_ports):
    """
    Create dynamic rows for outlet port sizes appearing under the outlet port number input.
    
    Args:
        frame: The parent frame to add rows to
        port_type: 'fuel' or 'oxidiser'
        num_ports: Number of ports to create
    """
    global fuel_outlet_port_entries, fuel_outlet_port_labels, oxidiser_outlet_port_entries, oxidiser_outlet_port_labels
    
    # Clear existing entries and labels
    if port_type == 'fuel':
        for entry in fuel_outlet_port_entries:
            entry.grid_forget()
        for label in fuel_outlet_port_labels:
            label.grid_forget()
        fuel_outlet_port_entries = []
        fuel_outlet_port_labels = []
        entries_list = fuel_outlet_port_entries
        labels_list = fuel_outlet_port_labels
    else:
        for entry in oxidiser_outlet_port_entries:
            entry.grid_forget()
        for label in oxidiser_outlet_port_labels:
            label.grid_forget()
        oxidiser_outlet_port_entries = []
        oxidiser_outlet_port_labels = []
        entries_list = oxidiser_outlet_port_entries
        labels_list = oxidiser_outlet_port_labels
    
    # Create new entries
    try:
        num = int(num_ports)
        
        # Calculate starting row - after outlet port number input
        outlet_label_row = Cap_Outlet_Ports.grid_info()['row']
        col = 1 if port_type == 'fuel' else 3
        start_row = outlet_label_row + 1
        
        for i in range(num):
            port_label = ttk.Label(frame, text=f"Port {i+1} Size (in):")
            port_label.grid(row=start_row + i, column=col-1, padx=5, pady=3, sticky=tk.E)
            labels_list.append(port_label)
            
            port_entry = tk.Entry(frame, width=10, bg='lightblue', fg='black')
            port_entry.grid(row=start_row + i, column=col, padx=5, pady=3)
            entries_list.append(port_entry)
    except (ValueError, TypeError):
        pass

root = tk.Tk()
root.title("Tank Sizer")
root.geometry() 

root.lift() # Bring the window to the front
root.attributes("-topmost", True) # Keep the window on top
root.focus_force() # After 2 seconds, allow other windows to be on top again

def release_topmost(): # Function to release the topmost attribute
    root.attributes("-topmost", False) # Allow other windows to be on top again

root.after(2000, release_topmost) # Release the topmost attribute after 2 seconds

#########################################################################################
################################# Conversion Factors #################################
#########################################################################################

# Pressure Conversions
psi_pa = 6894.76 # 1 psi = 6894.76 Pa
pa_psi = 1 / psi_pa # 1 Pa = 0.000145038 psi
psi_bar = 0.0689476 # 1 psi = 0.0689476 bar
bar_psi = 14.5038 # 1 bar = 14.5038 psi
MPa_Pa = 1e6 # 1 MPa = 1,000,000 Pa
Pa_MPa = 1e-6 # 1 Pa = 0.000001 MPa

# Length Conversions
in_m = 0.0254 # 1 inch = 0.0254 m
m_in = 39.3701 # 1 meter = 39.3701 inches
in_cm = 2.54 # 1 inch = 2.54 cm
cm_in = 0.393701 # 1 cm = 0.393701 inches
in_mm = 25.4 # 1 inch = 25.4 mm
mm_in = 0.0393701 # 1 mm = 0.0393701 inches
ft_m = 0.3048 # 1 foot = 0.3048 m
m_ft = 3.28084 # 1 meter = 3.28084 feet

# Mass Conversions
lb_kg = 0.453592 # 1 lb = 0.453592 kg
kgs_lbm = 2.20462 # 1 kg = 2.20462 lb
oz_g = 28.3495 # 1 ounce = 28.3495 grams
g_oz = 0.035274 # 1 gram = 0.035274 ounces

# Density Conversions
kgm3_lbmft3 = 0.062428 # 1 kg/m³ = 0.062428 lb/ft³
lbmft3_kgm3 = 16.0185 # 1 lb/ft³ = 16.0185 kg/m³
kgm3_lbmin3 = 3.6127e-5 # 1 kg/m³ = 3.6127e-5 lb/in³
lbmin3_kgm3 = 27680 # 1 lb/in³ = 27680 kg/m³

# Volume Conversions
in3_cm3 = 16.3871 # 1 cubic inch = 16.3871 cm³
cm3_in3 = 0.0610237 # 1 cm³ = 0.0610237 cubic inches
in3_L = 0.0163871 # 1 cubic inch = 0.0163871 liters
L_in3 = 61.0237 # 1 liter = 61.0237 cubic inches
L_m3 = 0.001 # 1 liter = 0.001 m³
m3_L = 1000 # 1 m³ = 1000 liters
gal_L = 3.78541 # 1 US gallon = 3.78541 liters
L_gal = 0.264172 # 1 liter = 0.264172 US gallons

# Stress/Force Conversions
psi_MPa = 0.00689476 # 1 psi = 0.00689476 MPa
MPa_psi = 145.038 # 1 MPa = 145.038 psi
ksi_MPa = 6.89476 # 1 ksi = 6.89476 MPa
MPa_ksi = 0.145038 # 1 MPa = 0.145038 ksi


#########################################################################################
################################# Pre-set all variables #################################
#########################################################################################

# Density (INPUT)
fuel_density_INPUT = tk.DoubleVar()
oxidiser_density_INPUT = tk.DoubleVar()
propellant_density_units = tk.StringVar()
fuel_density_kgm3 = tk.DoubleVar()
fuel_density_lbft3 = tk.DoubleVar()
fuel_density_lbin3 = tk.DoubleVar()
oxidiser_density_kgm3 = tk.DoubleVar()
oxidiser_density_lbft3 = tk.DoubleVar()
oxidiser_density_lbin3 = tk.DoubleVar()

# Mass Flow Rate (INPUT)
fuel_mass_flow_INPUT = tk.DoubleVar()
oxidiser_mass_flow_INPUT = tk.DoubleVar()
mass_flow_units = tk.StringVar()
fuel_mass_flow_kgs = tk.DoubleVar()
fuel_mass_flow_lbs = tk.DoubleVar()
oxidiser_mass_flow_kgs = tk.DoubleVar()
oxidiser_mass_flow_lbs = tk.DoubleVar()

# Vehicle Diameter (INPUT)
vehicle_diameter_INPUT = tk.DoubleVar()
diameter_units = tk.StringVar()
vehicle_diameter_in = tk.DoubleVar()
vehicle_diameter_mm = tk.DoubleVar()
vehicle_diameter_m = tk.DoubleVar()

# MEOP (INPUT)
fuel_meop_INPUT = tk.DoubleVar()
oxidiser_meop_INPUT = tk.DoubleVar()
meop_units = tk.StringVar()
fuel_meop_psi = tk.DoubleVar()
fuel_meop_Pa = tk.DoubleVar()
oxidiser_meop_psi = tk.DoubleVar()
oxidiser_meop_Pa = tk.DoubleVar()

# Weld Efficiency (INPUT)
weld_efficiency = tk.DoubleVar()

# Allowable Stress (INPUT)
allowable_stress_INPUT = tk.DoubleVar()
stress_units = tk.StringVar()
allowable_stress_Pa = tk.DoubleVar()
allowable_stress_MPa = tk.DoubleVar()
allowable_stress_psi = tk.DoubleVar()
allowable_stress_ksi = tk.DoubleVar()

# Run Time (INPUT)
run_time = tk.DoubleVar()

# Ullage (INPUT)
fuel_ullage = tk.DoubleVar()
oxidiser_ullage = tk.DoubleVar()

# Cap Skirt Length (INPUT)
fuel_cap_skirt_INPUT = tk.DoubleVar()
fuel_cap_skirt_in = tk.DoubleVar()
fuel_cap_skirt_mm = tk.DoubleVar()
fuel_cap_skirt_m = tk.DoubleVar()
oxidiser_cap_skirt_INPUT = tk.DoubleVar()
oxidiser_cap_skirt_in = tk.DoubleVar()
oxidiser_cap_skirt_mm = tk.DoubleVar()
oxidiser_cap_skirt_m = tk.DoubleVar()
cap_skirt_units = tk.StringVar()

# OUTPUT VARIABLES
# Tank Dimensions
oxidiser_tank_outer_diameter_in = tk.DoubleVar()
oxidiser_tank_outer_diameter_mm = tk.DoubleVar()
oxidiser_tank_outer_diameter_m = tk.DoubleVar()
fuel_tank_outer_diameter_in = tk.DoubleVar()
fuel_tank_outer_diameter_mm = tk.DoubleVar()
fuel_tank_outer_diameter_m = tk.DoubleVar()
tank_outer_diameter_units = tk.StringVar()
oxidiser_tank_inner_diameter_in = tk.DoubleVar()
oxidiser_tank_inner_diameter_mm = tk.DoubleVar()
oxidiser_tank_inner_diameter_m = tk.DoubleVar()
fuel_tank_inner_diameter_in = tk.DoubleVar()
fuel_tank_inner_diameter_mm = tk.DoubleVar()
fuel_tank_inner_diameter_m = tk.DoubleVar()
tank_inner_diameter_units = tk.StringVar()
oxidiser_wall_thickness_in = tk.DoubleVar()
oxidiser_wall_thickness_mm = tk.DoubleVar()
oxidiser_wall_thickness_m = tk.DoubleVar()
fuel_wall_thickness_in = tk.DoubleVar()
fuel_wall_thickness_mm = tk.DoubleVar()
fuel_wall_thickness_m = tk.DoubleVar()
wall_thickness_units = tk.StringVar()

# Propellant Mass (OUTPUT)
oxidiser_propellant_mass_lb = tk.DoubleVar()
oxidiser_propellant_mass_kg = tk.DoubleVar()
fuel_propellant_mass_lb = tk.DoubleVar()
fuel_propellant_mass_kg = tk.DoubleVar()
propellant_mass_units = tk.StringVar()

# Propellant Volume (OUTPUT)
oxidiser_propellant_volume_L = tk.DoubleVar()
oxidiser_propellant_volume_in3 = tk.DoubleVar()
oxidiser_propellant_volume_m3 = tk.DoubleVar()
fuel_propellant_volume_L = tk.DoubleVar()
fuel_propellant_volume_in3 = tk.DoubleVar()
fuel_propellant_volume_m3 = tk.DoubleVar()
propellant_volume_units = tk.StringVar()

# Required Volume (OUTPUT)
oxidiser_required_volume_L = tk.DoubleVar()
oxidiser_required_volume_in3 = tk.DoubleVar()
oxidiser_required_volume_m3 = tk.DoubleVar()
fuel_required_volume_L = tk.DoubleVar()
fuel_required_volume_in3 = tk.DoubleVar()
fuel_required_volume_m3 = tk.DoubleVar()
required_volume_units = tk.StringVar()

# Shell Volume (OUTPUT)
oxidiser_shell_volume_L = tk.DoubleVar()
oxidiser_shell_volume_in3 = tk.DoubleVar()
oxidiser_shell_volume_m3 = tk.DoubleVar()
fuel_shell_volume_L = tk.DoubleVar()
fuel_shell_volume_in3 = tk.DoubleVar()
fuel_shell_volume_m3 = tk.DoubleVar()
shell_volume_units = tk.StringVar()

# Tank Internal Height (OUTPUT)
oxidiser_internal_height_in = tk.DoubleVar()
oxidiser_internal_height_mm = tk.DoubleVar()
oxidiser_internal_height_m = tk.DoubleVar()
fuel_internal_height_in = tk.DoubleVar()
fuel_internal_height_mm = tk.DoubleVar()
fuel_internal_height_m = tk.DoubleVar()
internal_height_units = tk.StringVar()

# Stress (OUTPUT)
oxidiser_hoop_stress = tk.DoubleVar()
fuel_hoop_stress = tk.DoubleVar()
oxidiser_axial_stress = tk.DoubleVar()
fuel_axial_stress = tk.DoubleVar()

# Cap Dimensions (OUTPUT)
oxidiser_cap_thickness_in = tk.DoubleVar()
oxidiser_cap_thickness_mm = tk.DoubleVar()
oxidiser_cap_thickness_m = tk.DoubleVar()
fuel_cap_thickness_in = tk.DoubleVar()
fuel_cap_thickness_mm = tk.DoubleVar()
fuel_cap_thickness_m = tk.DoubleVar()
cap_thickness_units = tk.StringVar()
oxidiser_cap_height_in = tk.DoubleVar()
oxidiser_cap_height_mm = tk.DoubleVar()
oxidiser_cap_height_m = tk.DoubleVar()
fuel_cap_height_in = tk.DoubleVar()
fuel_cap_height_mm = tk.DoubleVar()
fuel_cap_height_m = tk.DoubleVar()
cap_height_units = tk.StringVar()
oxidiser_cap_knuckle_radius_in = tk.DoubleVar()
oxidiser_cap_knuckle_radius_mm = tk.DoubleVar()
oxidiser_cap_knuckle_radius_m = tk.DoubleVar()
fuel_cap_knuckle_radius_in = tk.DoubleVar()
fuel_cap_knuckle_radius_mm = tk.DoubleVar()
fuel_cap_knuckle_radius_m = tk.DoubleVar()
cap_knuckle_radius_units = tk.StringVar()
oxidiser_cap_crown_radius_in = tk.DoubleVar()
oxidiser_cap_crown_radius_mm = tk.DoubleVar()
oxidiser_cap_crown_radius_m = tk.DoubleVar()
fuel_cap_crown_radius_in = tk.DoubleVar()
fuel_cap_crown_radius_mm = tk.DoubleVar()
fuel_cap_crown_radius_m = tk.DoubleVar()
cap_crown_radius_units = tk.StringVar()
oxidiser_cap_volume_L = tk.DoubleVar()
oxidiser_cap_volume_in3 = tk.DoubleVar()
oxidiser_cap_volume_m3 = tk.DoubleVar()
fuel_cap_volume_L = tk.DoubleVar()
fuel_cap_volume_in3 = tk.DoubleVar()
fuel_cap_volume_m3 = tk.DoubleVar()
cap_volume_units = tk.StringVar()

fuel_cap_outlet_port_number = tk.IntVar()
fuel_cap_outlet_port_diameter_in = tk.DoubleVar()
fuel_cap_outlet_port_diameter_mm = tk.DoubleVar()
oxidiser_cap_outlet_port_number = tk.IntVar()
oxidiser_cap_outlet_port_diameter_in = tk.DoubleVar()
oxidiser_cap_outlet_port_diameter_mm = tk.DoubleVar()

fuel_cap_inlet_port_number = tk.IntVar()
fuel_cap_inlet_port_diameter_in = tk.DoubleVar() 
fuel_cap_inlet_port_diameter_mm = tk.DoubleVar()
oxidiser_cap_inlet_port_number = tk.IntVar()
oxidiser_cap_inlet_port_diameter_in = tk.DoubleVar()
oxidiser_cap_inlet_port_diameter_mm = tk.DoubleVar()

# Lists to store dynamic inlet port entry widgets and labels
fuel_inlet_port_entries = []
fuel_inlet_port_labels = []
oxidiser_inlet_port_entries = []
oxidiser_inlet_port_labels = []  

fuel_outlet_port_entries = []
fuel_outlet_port_labels = []
oxidiser_outlet_port_entries = []
oxidiser_outlet_port_labels = []  

# Operating Pressures (OUTPUT)
oxidiser_mawp_circ_psi = tk.DoubleVar()
oxidiser_mawp_circ_Pa = tk.DoubleVar()
fuel_mawp_circ_psi = tk.DoubleVar()
fuel_mawp_circ_Pa = tk.DoubleVar()
mawp_circ_units = tk.StringVar()
oxidiser_mawp_long_psi = tk.DoubleVar()
oxidiser_mawp_long_Pa = tk.DoubleVar()
fuel_mawp_long_psi = tk.DoubleVar()
fuel_mawp_long_Pa = tk.DoubleVar()
mawp_long_units = tk.StringVar()
oxidiser_hydro_pressure_psi = tk.DoubleVar()
oxidiser_hydro_pressure_Pa = tk.DoubleVar()
fuel_hydro_pressure_psi = tk.DoubleVar()
fuel_hydro_pressure_Pa = tk.DoubleVar()
hydro_pressure_units = tk.StringVar()
oxidiser_relief_pressure_psi = tk.DoubleVar()
oxidiser_relief_pressure_Pa = tk.DoubleVar()
fuel_relief_pressure_psi = tk.DoubleVar()
fuel_relief_pressure_Pa = tk.DoubleVar()
relief_pressure_units = tk.StringVar()
oxidiser_mawp_long_Pa = tk.DoubleVar()
fuel_mawp_long_psi = tk.DoubleVar()
fuel_mawp_long_Pa = tk.DoubleVar()
mawp_long_units = tk.StringVar()
oxidiser_hydro_pressure_psi = tk.DoubleVar()
oxidiser_hydro_pressure_Pa = tk.DoubleVar()
fuel_hydro_pressure_psi = tk.DoubleVar()
fuel_hydro_pressure_Pa = tk.DoubleVar()
hydro_pressure_units = tk.StringVar()
oxidiser_relief_pressure_psi = tk.DoubleVar()
oxidiser_relief_pressure_Pa = tk.DoubleVar()
fuel_relief_pressure_psi = tk.DoubleVar()
fuel_relief_pressure_Pa = tk.DoubleVar()
relief_pressure_units = tk.StringVar()

Export_units = tk.StringVar()

#########################################################################################
################################### Dictionary ##########################################
#########################################################################################

variables = {
    # Density
    'fuel_density': {'kg/m³': fuel_density_kgm3, 'lb/ft³': fuel_density_lbft3, 'lb/in³': fuel_density_lbin3},
    'oxidiser_density': {'kg/m³': oxidiser_density_kgm3, 'lb/ft³': oxidiser_density_lbft3, 'lb/in³': oxidiser_density_lbin3},
    
    # Mass Flow Rate
    'fuel_mass_flow': {'kg/s': fuel_mass_flow_kgs, 'lb/s': fuel_mass_flow_lbs},
    'oxidiser_mass_flow': {'kg/s': oxidiser_mass_flow_kgs, 'lb/s': oxidiser_mass_flow_lbs},

    # Vehicle Diameter
    'vehicle_diameter': {'in': vehicle_diameter_in, 'mm': vehicle_diameter_mm, 'm': vehicle_diameter_m},

    # MEOP
    'fuel_meop': {'psi': fuel_meop_psi, 'Pa': fuel_meop_Pa},
    'oxidiser_meop': {'psi': oxidiser_meop_psi, 'Pa': oxidiser_meop_Pa},

    # Allowable Stress
    'allowable_stress': {'Pa': allowable_stress_Pa, 'MPa': allowable_stress_MPa, 'psi': allowable_stress_psi, 'ksi': allowable_stress_ksi},

    # Cap Skirt Length
    'fuel_cap_skirt': {'in': fuel_cap_skirt_in, 'mm': fuel_cap_skirt_mm, 'm': fuel_cap_skirt_m},
    'oxidiser_cap_skirt': {'in': oxidiser_cap_skirt_in, 'mm': oxidiser_cap_skirt_mm, 'm': oxidiser_cap_skirt_m},
    
    # Tank Outer Diameter
    'fuel_tank_outer_diameter': {'in': fuel_tank_outer_diameter_in, 'mm': fuel_tank_outer_diameter_mm, 'm': fuel_tank_outer_diameter_m},
    'oxidiser_tank_outer_diameter': {'in': oxidiser_tank_outer_diameter_in, 'mm': oxidiser_tank_outer_diameter_mm, 'm': oxidiser_tank_outer_diameter_m},
    
    # Tank Inner Diameter
    'fuel_tank_inner_diameter': {'in': fuel_tank_inner_diameter_in, 'mm': fuel_tank_inner_diameter_mm, 'm': fuel_tank_inner_diameter_m},
    'oxidiser_tank_inner_diameter': {'in': oxidiser_tank_inner_diameter_in, 'mm': oxidiser_tank_inner_diameter_mm, 'm': oxidiser_tank_inner_diameter_m},
    
    # Wall Thickness
    'fuel_wall_thickness': {'in': fuel_wall_thickness_in, 'mm': fuel_wall_thickness_mm, 'm': fuel_wall_thickness_m},
    'oxidiser_wall_thickness': {'in': oxidiser_wall_thickness_in, 'mm': oxidiser_wall_thickness_mm, 'm': oxidiser_wall_thickness_m},
    
    # Propellant Mass
    'fuel_propellant_mass': {'lb': fuel_propellant_mass_lb, 'kg': fuel_propellant_mass_kg},
    'oxidiser_propellant_mass': {'lb': oxidiser_propellant_mass_lb, 'kg': oxidiser_propellant_mass_kg},
    
    # Propellant Volume
    'fuel_propellant_volume': {'L': fuel_propellant_volume_L, 'in³': fuel_propellant_volume_in3, 'm³': fuel_propellant_volume_m3},
    'oxidiser_propellant_volume': {'L': oxidiser_propellant_volume_L, 'in³': oxidiser_propellant_volume_in3, 'm³': oxidiser_propellant_volume_m3},
    
    # Required Volume
    'fuel_required_volume': {'L': fuel_required_volume_L, 'in³': fuel_required_volume_in3, 'm³': fuel_required_volume_m3},
    'oxidiser_required_volume': {'L': oxidiser_required_volume_L, 'in³': oxidiser_required_volume_in3, 'm³': oxidiser_required_volume_m3},
    
    # Shell Volume
    'fuel_shell_volume': {'L': fuel_shell_volume_L, 'in³': fuel_shell_volume_in3, 'm³': fuel_shell_volume_m3},
    'oxidiser_shell_volume': {'L': oxidiser_shell_volume_L, 'in³': oxidiser_shell_volume_in3, 'm³': oxidiser_shell_volume_m3},
    
    # Tank Internal Height
    'fuel_internal_height': {'in': fuel_internal_height_in, 'mm': fuel_internal_height_mm, 'm': fuel_internal_height_m},
    'oxidiser_internal_height': {'in': oxidiser_internal_height_in, 'mm': oxidiser_internal_height_mm, 'm': oxidiser_internal_height_m},
    
    # Cap Thickness
    'fuel_cap_thickness': {'in': fuel_cap_thickness_in, 'mm': fuel_cap_thickness_mm, 'm': fuel_cap_thickness_m},
    'oxidiser_cap_thickness': {'in': oxidiser_cap_thickness_in, 'mm': oxidiser_cap_thickness_mm, 'm': oxidiser_cap_thickness_m},
    
    # Cap Height
    'fuel_cap_height': {'in': fuel_cap_height_in, 'mm': fuel_cap_height_mm, 'm': fuel_cap_height_m},
    'oxidiser_cap_height': {'in': oxidiser_cap_height_in, 'mm': oxidiser_cap_height_mm, 'm': oxidiser_cap_height_m},
    
    # Cap Knuckle Radius
    'fuel_cap_knuckle_radius': {'in': fuel_cap_knuckle_radius_in, 'mm': fuel_cap_knuckle_radius_mm, 'm': fuel_cap_knuckle_radius_m},
    'oxidiser_cap_knuckle_radius': {'in': oxidiser_cap_knuckle_radius_in, 'mm': oxidiser_cap_knuckle_radius_mm, 'm': oxidiser_cap_knuckle_radius_m},
    
    # Cap Crown Radius
    'fuel_cap_crown_radius': {'in': fuel_cap_crown_radius_in, 'mm': fuel_cap_crown_radius_mm, 'm': fuel_cap_crown_radius_m},
    'oxidiser_cap_crown_radius': {'in': oxidiser_cap_crown_radius_in, 'mm': oxidiser_cap_crown_radius_mm, 'm': oxidiser_cap_crown_radius_m},
    
    # Cap Volume
    'fuel_cap_volume': {'L': fuel_cap_volume_L, 'in³': fuel_cap_volume_in3, 'm³': fuel_cap_volume_m3},
    'oxidiser_cap_volume': {'L': oxidiser_cap_volume_L, 'in³': oxidiser_cap_volume_in3, 'm³': oxidiser_cap_volume_m3},
    
    # MAWP Circumferential
    'fuel_mawp_circ': {'psi': fuel_mawp_circ_psi, 'Pa': fuel_mawp_circ_Pa},
    'oxidiser_mawp_circ': {'psi': oxidiser_mawp_circ_psi, 'Pa': oxidiser_mawp_circ_Pa},
    
    # MAWP Longitudinal
    'fuel_mawp_long': {'psi': fuel_mawp_long_psi, 'Pa': fuel_mawp_long_Pa},
    'oxidiser_mawp_long': {'psi': oxidiser_mawp_long_psi, 'Pa': oxidiser_mawp_long_Pa},
    
    # Hydro Pressure
    'fuel_hydro_pressure': {'psi': fuel_hydro_pressure_psi, 'Pa': fuel_hydro_pressure_Pa},
    'oxidiser_hydro_pressure': {'psi': oxidiser_hydro_pressure_psi, 'Pa': oxidiser_hydro_pressure_Pa},
    
    # Relief Pressure
    'fuel_relief_pressure': {'psi': fuel_relief_pressure_psi, 'Pa': fuel_relief_pressure_Pa},
    'oxidiser_relief_pressure': {'psi': oxidiser_relief_pressure_psi, 'Pa': oxidiser_relief_pressure_Pa},
}




#########################################################################################
############################# Pre-set Default Values ####################################
#########################################################################################

# Set default constraint values
fuel_density_INPUT.set(770)  # kg/m³
oxidiser_density_INPUT.set(1141)  # kg/m³
fuel_mass_flow_INPUT.set(3.365)  # kg/s
oxidiser_mass_flow_INPUT.set(6.731)  # kg/s
vehicle_diameter_INPUT.set(12)  # inches
fuel_meop_INPUT.set(1000)  # psi
oxidiser_meop_INPUT.set(850)  # psi
weld_efficiency.set(0.8)  # 80% efficiency
run_time.set(30)  # seconds
fuel_ullage.set(6)  # 6% ullage
oxidiser_ullage.set(6)  # 6% ullage
allowable_stress_INPUT.set(82.7)  # MPa
fuel_cap_skirt_INPUT.set(0.5) # inch
oxidiser_cap_skirt_INPUT.set(0.5) # inch

propellant_density_units.set("kg/m³")
mass_flow_units.set("kg/s")
diameter_units.set("in")
tank_outer_diameter_units.set("in")
tank_inner_diameter_units.set("in")
wall_thickness_units.set("in")
meop_units.set("Psi")
stress_units.set("MPa")
cap_skirt_units.set("in")
cap_knuckle_radius_units.set("in")
cap_crown_radius_units.set("in")
propellant_mass_units.set("kg")
propellant_volume_units.set("L")
required_volume_units.set("L")
shell_volume_units.set("L")
internal_height_units.set("in")
cap_thickness_units.set("in")
cap_height_units.set("in")
cap_volume_units.set("L")
mawp_circ_units.set("Psi")
mawp_long_units.set("Psi")
hydro_pressure_units.set("Psi")
relief_pressure_units.set("Psi")


#########################################################################################
################################# Constraints Parameters ################################
#########################################################################################

Constraints_Container = ttk.Frame(root, relief=tk.RAISED, borderwidth=2)
Constraints_Container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

Constraints = ttk.Frame(Constraints_Container, padding="15")
Constraints.pack(fill=tk.BOTH, expand=True)
Constraints_label = ttk.Label(Constraints, text="CONSTRAINTS", font=("Arial", 14))
Constraints_label.grid(row=0, column=0, columnspan=3, pady=5)

## Create labels for fuel and oxidiser columns
Fuel_label = ttk.Label(Constraints, text="FUEL", font=("Arial", 10))
Fuel_label.grid(row=1, column=2, pady=5)
Oxidiser_label = ttk.Label(Constraints, text="OXIDISER", font=("Arial", 10))
Oxidiser_label.grid(row=1, column=3, pady=5)

##Density labels and entry widgets
Density_label = ttk.Label(Constraints, text="Density:")
Density_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
Density_units = ttk.Combobox(Constraints, textvariable=propellant_density_units, values=["kg/m³", "lb/ft³", "lb/in³"], state="readonly", width=5)
Density_units.grid(row=2, column=1, padx=5, pady=5)
fuel_density_entry = tk.Entry(Constraints, width=10, textvariable=fuel_density_INPUT, bg='lightgreen', fg='black')
fuel_density_entry.grid(row=2, column=2, padx=5, pady=5)
oxidiser_density_entry = tk.Entry(Constraints, width=10, textvariable=oxidiser_density_INPUT, bg='lightgreen', fg='black')
oxidiser_density_entry.grid(row=2, column=3, padx=5, pady=5)

##Mass flow rate labels and entry widgets

MassFlowRate_label = ttk.Label(Constraints, text="Mass Flow Rate:")
MassFlowRate_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
MassFlowRate_units = ttk.Combobox(Constraints, textvariable=mass_flow_units, values=["kg/s", "lb/s", "lb/min"], state="readonly", width=5)
MassFlowRate_units.grid(row=3, column=1, padx=5, pady=5)
fuel_mass_flow_entry = tk.Entry(Constraints, width=10, textvariable=fuel_mass_flow_INPUT, bg='lightgreen', fg='black')
fuel_mass_flow_entry.grid(row=3, column=2, padx=5, pady=5)
oxidiser_mass_flow_entry = tk.Entry(Constraints, width=10, textvariable=oxidiser_mass_flow_INPUT, bg='lightgreen', fg='black')
oxidiser_mass_flow_entry.grid(row=3, column=3, padx=5, pady=5)

##Vehicle Diameter labels and entry widgets 
Vehicle_Diameter_label = ttk.Label(Constraints, text="Vehicle Diameter:")
Vehicle_Diameter_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
Vehicle_Diameter_units = ttk.Combobox(Constraints, textvariable=diameter_units, values=["in", "mm"], state="readonly", width=5)
Vehicle_Diameter_units.grid(row=4, column=1, padx=5, pady=5)
fuel_vehicle_diameter_entry = tk.Entry(Constraints, width=10, textvariable=vehicle_diameter_INPUT, bg='lightgreen', fg='black')
fuel_vehicle_diameter_entry.grid(row=4, column=2, padx=5, pady=5)
oxidiser_vehicle_diameter_entry = tk.Entry(Constraints, width=10, textvariable=vehicle_diameter_INPUT, bg='lightgreen', fg='black')
oxidiser_vehicle_diameter_entry.grid(row=4, column=3, padx=5, pady=5)

##Maximum Expected Operating Pressure (MEOP) labels and entry widgets 
MEOP_label = ttk.Label(Constraints, text="MEOP:")
MEOP_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
MEOP_units = ttk.Combobox(Constraints, textvariable=meop_units, values=["Psi", "Pa", "bar"], state="readonly", width=5)
MEOP_units.grid(row=5, column=1, padx=5, pady=5)
fuel_MEOP_entry = tk.Entry(Constraints, width=10, textvariable=fuel_meop_INPUT, bg='lightgreen', fg='black')
fuel_MEOP_entry.grid(row=5, column=2, padx=5, pady=5)
oxidiser_MEOP_entry = tk.Entry(Constraints, width=10, textvariable=oxidiser_meop_INPUT, bg='lightgreen', fg='black')
oxidiser_MEOP_entry.grid(row=5, column=3, padx=5, pady=5)

##Weld Efficiency labels and entry widgets 
WeldEff_label = ttk.Label(Constraints, text="Weld Efficiency:")
WeldEff_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.E)
fuel_weld_eff_entry = tk.Entry(Constraints, width=10, textvariable=weld_efficiency, bg='lightgreen', fg='black')
fuel_weld_eff_entry.grid(row=6, column=2, padx=5, pady=5)
oxidiser_weld_eff_entry = tk.Entry(Constraints, width=10, textvariable=weld_efficiency, bg='lightgreen', fg='black')
oxidiser_weld_eff_entry.grid(row=6, column=3, padx=5, pady=5)

##Run Time labels and entry widgets 
RunTime_label = ttk.Label(Constraints, text="Run Time:")
RunTime_label.grid(row=7, column=0, padx=5, pady=5, sticky=tk.E)
fuel_run_time_entry = tk.Entry(Constraints, width=10, textvariable=run_time, bg='lightgreen', fg='black')
fuel_run_time_entry.grid(row=7, column=2, padx=5, pady=5)
oxidiser_run_time_entry = tk.Entry(Constraints, width=10, textvariable=run_time, bg='lightgreen', fg='black')
oxidiser_run_time_entry.grid(row=7, column=3, padx=5, pady=5)

##Ullage Percentage labels and entry widgets 
UllagePercent_label = ttk.Label(Constraints, text="Ullage Percentage:")
UllagePercent_label.grid(row=8, column=0, padx=5, pady=5, sticky=tk.E)
fuel_ullage_entry = tk.Entry(Constraints, width=10, textvariable=fuel_ullage, bg='lightgreen', fg='black')
fuel_ullage_entry.grid(row=8, column=2, padx=5, pady=5)
oxidiser_ullage_entry = tk.Entry(Constraints, width=10, textvariable=oxidiser_ullage, bg='lightgreen', fg='black')
oxidiser_ullage_entry.grid(row=8, column=3, padx=5, pady=5)

##Allowable Stress labels and entry widgets 
AllowableStress_label = ttk.Label(Constraints, text="Allowable Stress:")
AllowableStress_label.grid(row=9, column=0, padx=5, pady=5, sticky=tk.E)
S_fuel_entry = tk.Entry(Constraints, width=10, textvariable=allowable_stress_INPUT, bg='lightgreen', fg='black')
S_fuel_entry.grid(row=9, column=2, padx=5, pady=5)
S_oxidiser_entry = tk.Entry(Constraints, width=10, textvariable=allowable_stress_INPUT, bg='lightgreen', fg='black')
S_oxidiser_entry.grid(row=9, column=3, padx=5, pady=5)

#########################################################################################
################################# Calculation Outputs ################################
#########################################################################################

Calculation_outputs_Container = ttk.Frame(root, relief=tk.RAISED, borderwidth=2)
Calculation_outputs_Container.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

Calculation_outputs = ttk.Frame(Calculation_outputs_Container, padding="15")
Calculation_outputs.pack(fill=tk.BOTH, expand=True)
Calculation_outputs_label = ttk.Label(Calculation_outputs, text="CALCULATION OUTPUTS", font=("Arial", 14))
Calculation_outputs_label.grid(row=0, column=0, columnspan=4, pady=5)

## Create labels for fuel and oxidiser
Fuel_label = ttk.Label(Calculation_outputs, text="FUEL", font=("Arial", 10))
Fuel_label.grid(row=1, column=2, pady=5)
Oxidiser_label = ttk.Label(Calculation_outputs, text="OXIDISER", font=("Arial", 10))
Oxidiser_label.grid(row=1, column=3, pady=5)

Propellant_Mass_label = ttk.Label(Calculation_outputs, text="Propellant Mass:")
Propellant_Mass_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
Propellant_Mass_units = ttk.Combobox(Calculation_outputs, textvariable=propellant_mass_units , values=["lb", "kg"], state="readonly", width=5)
Propellant_Mass_units.grid(row=2, column=1, padx=5, pady=5)
Fuel_Propellant_Mass_entry = tk.Entry(Calculation_outputs, width=10, textvariable=fuel_propellant_mass_lb if propellant_mass_units.get() == "lb" else fuel_propellant_mass_kg, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_Propellant_Mass_entry.grid(row=2, column=2, padx=5, pady=5)
Oxidiser_Propellant_Mass_entry = tk.Entry(Calculation_outputs, width=10, textvariable=oxidiser_propellant_mass_lb if propellant_mass_units.get() == "lb" else oxidiser_propellant_mass_kg, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_Propellant_Mass_entry.grid(row=2, column=3, padx=5, pady=5)

Propellant_Volume_Label = ttk.Label(Calculation_outputs, text="Propellant Volume:")
Propellant_Volume_Label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
Propellant_Volume_units = ttk.Combobox(Calculation_outputs, textvariable=propellant_volume_units, values=["L", "m³", "gal", "in³"], state="readonly", width=5)
Propellant_Volume_units.grid(row=3, column=1, padx=5, pady=5)
Fuel_Propellant_Volume_entry = tk.Entry(Calculation_outputs, width=10, textvariable=fuel_propellant_volume_L if propellant_volume_units.get() == "L" else fuel_propellant_volume_m3, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_Propellant_Volume_entry.grid(row=3, column=2, padx=5, pady=5)
Oxidiser_Propellant_Volume_entry = tk.Entry(Calculation_outputs, width=10, textvariable=oxidiser_propellant_volume_L if propellant_volume_units.get() == "L" else oxidiser_propellant_volume_m3, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_Propellant_Volume_entry.grid(row=3, column=3, padx=5, pady=5)

Required_Tank_Volume_Label = ttk.Label(Calculation_outputs, text="Required Tank Volume w/Ullage:")
Required_Tank_Volume_Label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
Required_Volume_units = ttk.Combobox(Calculation_outputs, textvariable=required_volume_units, values=["L", "m³", "gal", "in³"], state="readonly", width=5)
Required_Volume_units.grid(row=4, column=1, padx=5, pady=5)
Fuel_Required_Tank_Volume_entry = tk.Entry(Calculation_outputs, width=10, textvariable=fuel_required_volume_L if required_volume_units.get() == "L" else fuel_required_volume_m3, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_Required_Tank_Volume_entry.grid(row=4, column=2, padx=5, pady=5)
Oxidiser_Required_Tank_Volume_entry = tk.Entry(Calculation_outputs, width=10, textvariable=oxidiser_required_volume_L if required_volume_units.get() == "L" else oxidiser_required_volume_m3, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_Required_Tank_Volume_entry.grid(row=4, column=3, padx=5, pady=5)

##########################################################################################
#################################### Tank Dimensions #####################################
##########################################################################################

#################################### Shell Dimensions ####################################

Tank_Container = ttk.Frame(root, relief=tk.RAISED, borderwidth=2)
Tank_Container.grid(row=0, column=1, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

Tank = ttk.Frame(Tank_Container, padding="15")
Tank.pack(fill=tk.BOTH, expand=True)
Tank_label = ttk.Label(Tank, text="Shell Dimensions", font=("Arial", 14))
Tank_label.grid(row=0, column=0, columnspan=4, pady=5)

## Create labels for fuel and oxidiser
Fuel_label = ttk.Label(Tank, text="FUEL", font=("Arial", 10))
Fuel_label.grid(row=1, column=2, pady=5)
Oxidiser_label = ttk.Label(Tank, text="OXIDISER", font=("Arial", 10))
Oxidiser_label.grid(row=1, column=3, pady=5)

Tank_Outer_Diameter_label = ttk.Label(Tank, text="Tank Outer Diameter:")
Tank_Outer_Diameter_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
Tank_Outer_Diameter_units = ttk.Combobox(Tank, textvariable=tank_outer_diameter_units, values=["in", "mm"], state="readonly", width=5)
Tank_Outer_Diameter_units.grid(row=2, column=1, padx=5, pady=5)
Fuel_Tank_Outer_Diameter_entry = tk.Entry(Tank, width=10, textvariable=fuel_tank_outer_diameter_in if tank_outer_diameter_units.get() == "in" else fuel_tank_outer_diameter_mm, state='readonly', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_Tank_Outer_Diameter_entry.grid(row=2, column=2, padx=5, pady=5)
Oxidiser_Tank_Outer_Diameter_entry = tk.Entry(Tank, width=10, textvariable=oxidiser_tank_outer_diameter_in if tank_outer_diameter_units.get() == "in" else oxidiser_tank_outer_diameter_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_Tank_Outer_Diameter_entry.grid(row=2, column=3, padx=5, pady=5)

Tank_Inner_Diameter_label = ttk.Label(Tank, text="Tank Inner Diameter:")
Tank_Inner_Diameter_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
Tank_Inner_Diameter_units = ttk.Combobox(Tank, textvariable=tank_inner_diameter_units, values=["in", "mm"], state="readonly", width=5)
Tank_Inner_Diameter_units.grid(row=3, column=1, padx=5, pady=5)
Fuel_tank_inner_diameter_entry = tk.Entry(Tank, width=10, textvariable=fuel_tank_inner_diameter_in if tank_inner_diameter_units.get() == "in" else fuel_tank_inner_diameter_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_tank_inner_diameter_entry.grid(row=3, column=2, padx=5, pady=5)
Oxidiser_tank_inner_diameter_entry = tk.Entry(Tank, width=10, textvariable=oxidiser_tank_inner_diameter_in if tank_inner_diameter_units.get() == "in" else oxidiser_tank_inner_diameter_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_tank_inner_diameter_entry.grid(row=3, column=3, padx=5, pady=5)

Tank_Wall_Thickness_label = ttk.Label(Tank, text="Tank Wall Thickness:")
Tank_Wall_Thickness_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
Tank_Wall_Thickness_units = ttk.Combobox(Tank, textvariable=wall_thickness_units, values=["in", "mm"], state="readonly", width=5)
Tank_Wall_Thickness_units.grid(row=4, column=1, padx=5, pady=5)
Fuel_tank_wall_thickness_entry = tk.Entry(Tank, width=10, textvariable=fuel_wall_thickness_in if wall_thickness_units.get() == "in" else fuel_wall_thickness_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_tank_wall_thickness_entry.grid(row=4, column=2, padx=5, pady=5)
Oxidiser_tank_wall_thickness_entry = tk.Entry(Tank, width=10, textvariable=oxidiser_wall_thickness_in if wall_thickness_units.get() == "in" else oxidiser_wall_thickness_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_tank_wall_thickness_entry.grid(row=4, column=3, padx=5, pady=5)

Shell_Volume_Label = ttk.Label(Tank, text="Shell Volume:")
Shell_Volume_Label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
Shell_Volume_units = ttk.Combobox(Tank, textvariable=shell_volume_units, values=["L", "m³", "gal", "in³"], state="readonly", width=5)
Shell_Volume_units.grid(row=5, column=1, padx=5, pady=5)
Fuel_Shell_Volume_entry = tk.Entry(Tank, width=10, textvariable=fuel_shell_volume_L, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_Shell_Volume_entry.grid(row=5, column=2, padx=5, pady=5)   
Oxidiser_Shell_Volume_entry = tk.Entry(Tank, width=10, textvariable=oxidiser_shell_volume_L, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_Shell_Volume_entry.grid(row=5, column=3, padx=5, pady=5)

Shell_Height_Label = ttk.Label(Tank, text="Internal Shell Height:")
Shell_Height_Label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.E)
Internal_Height_units = ttk.Combobox(Tank, textvariable=internal_height_units, values=["in", "mm"], state="readonly", width=5)
Internal_Height_units.grid(row=6, column=1, padx=5, pady=5)
Fuel_Shell_Height_entry = tk.Entry(Tank, width=10, textvariable=fuel_internal_height_in if internal_height_units.get() == "in" else fuel_internal_height_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_Shell_Height_entry.grid(row=6, column=2, padx=5, pady=5)   
Oxidiser_Shell_Height_entry = tk.Entry(Tank, width=10, textvariable=oxidiser_internal_height_in if internal_height_units.get() == "in" else oxidiser_internal_height_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_Shell_Height_entry.grid(row=6, column=3, padx=5, pady=5)

#################################### Cap Dimensions ####################################

Tank_caps_label = ttk.Label(Tank, text="Cap Dimensions", font=("Arial", 14))
Tank_caps_label.grid(row=7, column=0, columnspan=4, pady=5)

## Create labels for fuel and oxidiser
Fuel_label = ttk.Label(Tank, text="FUEL", font=("Arial", 10))
Fuel_label.grid(row=8, column=2, pady=5)
Oxidiser_label = ttk.Label(Tank, text="OXIDISER", font=("Arial", 10))
Oxidiser_label.grid(row=8, column=3, pady=5)

Cap_Minimum_Thickness_label = ttk.Label(Tank, text="Cap Minimum Thickness:")
Cap_Minimum_Thickness_label.grid(row=9, column=0, padx=5, pady=5, sticky=tk.E)
Cap_Thickness_units = ttk.Combobox(Tank, textvariable=cap_thickness_units, values=["in", "mm"], state="readonly", width=5)
Cap_Thickness_units.grid(row=9, column=1, padx=5, pady=5)
Fuel_Cap_Minimum_Thickness_entry = tk.Entry(Tank, width=10, textvariable=fuel_cap_thickness_in if cap_thickness_units.get() == "in" else fuel_cap_thickness_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_Cap_Minimum_Thickness_entry.grid(row=9, column=2, padx=5, pady=5)
Oxidiser_Cap_Minimum_Thickness_entry = tk.Entry(Tank, width=10, textvariable=oxidiser_cap_thickness_in if cap_thickness_units.get() == "in" else oxidiser_cap_thickness_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_Cap_Minimum_Thickness_entry.grid(row=9, column=3, padx=5, pady=5)

Cap_Skirt_Length_label = ttk.Label(Tank, text="Cap Skirt Length:")
Cap_Skirt_Length_label.grid(row=10, column=0, padx=5, pady=5, sticky=tk.E)
Cap_Skirt_units = ttk.Combobox(Tank, textvariable=cap_skirt_units, values=["in", "mm"], state="readonly", width=5)
Cap_Skirt_units.grid(row=10, column=1, padx=5, pady=5)
Fuel_Cap_Skirt_Length_entry = tk.Entry(Tank, width=10, textvariable=fuel_cap_skirt_INPUT, bg='lightgreen', fg='black')
Fuel_Cap_Skirt_Length_entry.grid(row=10, column=2, padx=5, pady=5)
Oxidiser_Cap_Skirt_Length_entry = tk.Entry(Tank, width=10, textvariable=oxidiser_cap_skirt_INPUT, bg='lightgreen', fg='black')
Oxidiser_Cap_Skirt_Length_entry.grid(row=10, column=3, padx=5, pady=5)

Cap_Head_Height_label = ttk.Label(Tank, text="Cap Head Height:")
Cap_Head_Height_label.grid(row=11, column=0, padx=5, pady=5, sticky=tk.E)
Cap_Height_units = ttk.Combobox(Tank, textvariable=cap_height_units, values=["in", "mm"], state="readonly", width=5)
Cap_Height_units.grid(row=11, column=1, padx=5, pady=5)
Fuel_Cap_Head_Height_entry = tk.Entry(Tank, width=10, textvariable=fuel_cap_height_in if cap_height_units.get() == "in" else fuel_cap_height_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_Cap_Head_Height_entry.grid(row=11, column=2, padx=5, pady=5)
Oxidiser_Cap_Head_Height_entry = tk.Entry(Tank, width=10, textvariable=oxidiser_cap_height_in if cap_height_units.get() == "in" else oxidiser_cap_height_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_Cap_Head_Height_entry.grid(row=11, column=3, padx=5, pady=5)

Cap_Knuckle_Radius_label = ttk.Label(Tank, text="Cap Knuckle Radius:")
Cap_Knuckle_Radius_label.grid(row=12, column=0, padx=5, pady=5, sticky=tk.E)
Cap_Knuckle_Radius_units = ttk.Combobox(Tank, textvariable=cap_knuckle_radius_units, values=["in", "mm"], state="readonly", width=5)
Cap_Knuckle_Radius_units.grid(row=12, column=1, padx=5, pady=5)
Fuel_Cap_Knuckle_Radius_entry = tk.Entry(Tank, width=10, textvariable=fuel_cap_knuckle_radius_in if cap_knuckle_radius_units.get() == "in" else fuel_cap_knuckle_radius_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_Cap_Knuckle_Radius_entry.grid(row=12, column=2, padx=5, pady=5)
Oxidiser_Cap_Knuckle_Radius_entry = tk.Entry(Tank, width=10, textvariable=oxidiser_cap_knuckle_radius_in if cap_knuckle_radius_units.get() == "in" else oxidiser_cap_knuckle_radius_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_Cap_Knuckle_Radius_entry.grid(row=12, column=3, padx=5, pady=5)

Cap_Crown_Radius_label = ttk.Label(Tank, text="Cap Crown Radius:")
Cap_Crown_Radius_label.grid(row=13, column=0, padx=5, pady=5, sticky=tk.E)
Cap_Crown_Radius_units = ttk.Combobox(Tank, textvariable=cap_crown_radius_units, values=["in", "mm"], state="readonly", width=5)
Cap_Crown_Radius_units.grid(row=13, column=1, padx=5, pady=5)
Fuel_Cap_Crown_Radius_entry = tk.Entry(Tank, width=10, textvariable=fuel_cap_crown_radius_in if cap_crown_radius_units.get() == "in" else fuel_cap_crown_radius_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_Cap_Crown_Radius_entry.grid(row=13, column=2, padx=5, pady=5)
Oxidiser_Cap_Crown_Radius_entry = tk.Entry(Tank, width=10, textvariable=oxidiser_cap_crown_radius_in if cap_crown_radius_units.get() == "in" else oxidiser_cap_crown_radius_mm, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_Cap_Crown_Radius_entry.grid(row=13, column=3, padx=5, pady=5)

Cap_Volume_label = ttk.Label(Tank, text="Cap Volume:")
Cap_Volume_label.grid(row=14, column=0, padx=5, pady=5, sticky=tk.E)
Cap_Volume_units = ttk.Combobox(Tank, textvariable=cap_volume_units, values=["in³", "L"], state="readonly", width=5)
Cap_Volume_units.grid(row=14, column=1, padx=5, pady=5)
Fuel_Cap_Volume_entry = tk.Entry(Tank, width=10, textvariable=fuel_cap_volume_L, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_Cap_Volume_entry.grid(row=14, column=2, padx=5, pady=5)
Oxidiser_Cap_Volume_entry = tk.Entry(Tank, width=10, textvariable=oxidiser_cap_volume_L, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_Cap_Volume_entry.grid(row=14, column=3, padx=5, pady=5)

##########################################################################################
#################################### Cap Port Design #####################################
##########################################################################################

Cap_Container = ttk.Frame(root, relief=tk.RAISED, borderwidth=2)
Cap_Container.grid(row=2, column=1, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

Cap = ttk.Frame(Cap_Container, padding="15")
Cap.pack(fill=tk.BOTH, expand=True)
Cap_label = ttk.Label(Cap, text="Cap Parameters", font=("Arial", 14))
Cap_label.grid(row=0, column=0, columnspan=5, pady=5)

## Create labels for fuel and oxidiser
Fuel_label = ttk.Label(Cap, text="FUEL", font=("Arial", 10))
Fuel_label.grid(row=1, column=1, pady=5)
Oxidiser_label = ttk.Label(Cap, text="OXIDISER", font=("Arial", 10))
Oxidiser_label.grid(row=1, column=3, pady=5)

Cap_Inlet_Ports = ttk.Label(Cap, text="Number of Cap Inlet Ports:")
Cap_Inlet_Ports.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
Fuel_Cap_Inlet_Ports_entry = tk.Entry(Cap, width=10, textvariable=fuel_cap_inlet_port_number, bg='lightgreen', fg='black')
Fuel_Cap_Inlet_Ports_entry.grid(row=2, column=1, padx=5, pady=5)
Oxidiser_Cap_Inlet_Ports_entry = tk.Entry(Cap, width=10, textvariable=oxidiser_cap_inlet_port_number, bg='lightgreen', fg='black')
Oxidiser_Cap_Inlet_Ports_entry.grid(row=2, column=3, padx=5, pady=5)

# Bind events to create inlet port rows
def on_fuel_inlet_ports_change(event=None):
    create_inlet_port_rows(Cap, 'fuel', safe_int(fuel_cap_inlet_port_number))
    
def on_oxidiser_inlet_ports_change(event=None):
    create_inlet_port_rows(Cap, 'oxidiser', safe_int(oxidiser_cap_inlet_port_number))


Cap_Outlet_Ports = ttk.Label(Cap, text="Number of Cap Outlet Ports:")
Cap_Outlet_Ports.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
Fuel_Cap_Outlet_Ports_entry = tk.Entry(Cap, width=10, textvariable=fuel_cap_outlet_port_number, bg='lightgreen', fg='black')
Fuel_Cap_Outlet_Ports_entry.grid(row=3, column=1, padx=5, pady=5)
Oxidiser_Cap_Outlet_Ports_entry = tk.Entry(Cap, width=10, textvariable=oxidiser_cap_outlet_port_number, bg='lightgreen', fg='black')
Oxidiser_Cap_Outlet_Ports_entry.grid(row=3, column=3, padx=5, pady=5)

# Bind events to create outlet port rows
def on_fuel_outlet_ports_change(event=None):
    create_outlet_port_rows(Cap, 'fuel', safe_int(fuel_cap_outlet_port_number))
    
def on_oxidiser_outlet_ports_change(event=None):
    create_outlet_port_rows(Cap, 'oxidiser', safe_int(oxidiser_cap_outlet_port_number))


##########################################################################################
################################ PRESSURE REQUIREMENTS ###################################
##########################################################################################

Pressure_Container = ttk.Frame(root, relief=tk.RAISED, borderwidth=2)
Pressure_Container.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

Pressure_values = ttk.Frame(Pressure_Container, padding="15")
Pressure_values.pack(fill=tk.BOTH, expand=True)
Pressure_values_label = ttk.Label(Pressure_values, text="PRESSURE REQUIREMENTS", font=("Arial", 14))
Pressure_values_label.grid(row=0, column=0, columnspan=4, pady=5)

## Create labels for fuel and oxidiser
Fuel_label = ttk.Label(Pressure_values, text="FUEL", font=("Arial", 10))
Fuel_label.grid(row=1, column=2, pady=5)
Oxidiser_label = ttk.Label(Pressure_values, text="OXIDISER", font=("Arial", 10))
Oxidiser_label.grid(row=1, column=3, pady=5)

MAWP_Circumferential_label = ttk.Label(Pressure_values, text="MAWP Circumferential:")
MAWP_Circumferential_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.E)
MAWP_Circ_units = ttk.Combobox(Pressure_values, textvariable=mawp_circ_units, values=["Psi", "Pa"], state="readonly", width=5)
MAWP_Circ_units.grid(row=6, column=1, padx=5, pady=5)
Fuel_MAWP_Circumferential_entry = tk.Entry(Pressure_values, width=10, textvariable=fuel_mawp_circ_psi if mawp_circ_units.get() == "Psi" else fuel_mawp_circ_Pa, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_MAWP_Circumferential_entry.grid(row=6, column=2, padx=5, pady=5)
Oxidiser_MAWP_Circumferential_entry = tk.Entry(Pressure_values, width=10, textvariable=oxidiser_mawp_circ_psi if mawp_circ_units.get() == "Psi" else oxidiser_mawp_circ_Pa, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_MAWP_Circumferential_entry.grid(row=6, column=3, padx=5, pady=5)

MAWP_Longitudinal_label = ttk.Label(Pressure_values, text="MAWP Longitudinal:")
MAWP_Longitudinal_label.grid(row=7, column=0, padx=5, pady=5, sticky=tk.E)
MAWP_Long_units = ttk.Combobox(Pressure_values, textvariable=mawp_long_units, values=["Psi", "Pa"], state="readonly", width=5)
MAWP_Long_units.grid(row=7, column=1, padx=5, pady=5)
Fuel_MAWP_Longitudinal_entry = tk.Entry(Pressure_values, width=10, textvariable=fuel_mawp_long_psi if mawp_long_units.get() == "Psi" else fuel_mawp_long_Pa, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_MAWP_Longitudinal_entry.grid(row=7, column=2, padx=5, pady=5)
Oxidiser_MAWP_Longitudinal_entry = tk.Entry(Pressure_values, width=10, textvariable=oxidiser_mawp_long_psi if mawp_long_units.get() == "Psi" else oxidiser_mawp_long_Pa, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_MAWP_Longitudinal_entry.grid(row=7, column=3, padx=5, pady=5)

Hydrostatic_Pressure_label = ttk.Label(Pressure_values, text="Hydrostatic Pressure:")
Hydrostatic_Pressure_label.grid(row=8, column=0, padx=5, pady=5, sticky=tk.E)
Hydro_Pressure_units = ttk.Combobox(Pressure_values, textvariable=hydro_pressure_units, values=["Psi", "Pa"], state="readonly", width=5)
Hydro_Pressure_units.grid(row=8, column=1, padx=5, pady=5)
Fuel_Hydrostatic_Pressure_entry = tk.Entry(Pressure_values, width=10, textvariable=fuel_hydro_pressure_psi if hydro_pressure_units.get() == "Psi" else fuel_hydro_pressure_Pa, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_Hydrostatic_Pressure_entry.grid(row=8, column=2, padx=5, pady=5)
Oxidiser_Hydrostatic_Pressure_entry = tk.Entry(Pressure_values, width=10, textvariable=oxidiser_hydro_pressure_psi if hydro_pressure_units.get() == "Psi" else oxidiser_hydro_pressure_Pa, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_Hydrostatic_Pressure_entry.grid(row=8, column=3, padx=5, pady=5)

Relief_Pressure_label = ttk.Label(Pressure_values, text="Relief Pressure:")
Relief_Pressure_label.grid(row=9, column=0, padx=5, pady=5, sticky=tk.E)
Relief_Pressure_units = ttk.Combobox(Pressure_values, textvariable=relief_pressure_units, values=["Psi", "Pa"], state="readonly", width=5)
Relief_Pressure_units.grid(row=9, column=1, padx=5, pady=5)
Fuel_Relief_Pressure_entry = tk.Entry(Pressure_values, width=10, textvariable=fuel_relief_pressure_psi if relief_pressure_units.get() == "Psi" else fuel_relief_pressure_Pa, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Fuel_Relief_Pressure_entry.grid(row=9, column=2, padx=5, pady=5)
Oxidiser_Relief_Pressure_entry = tk.Entry(Pressure_values, width=10, textvariable=oxidiser_relief_pressure_psi if relief_pressure_units.get() == "Psi" else oxidiser_relief_pressure_Pa, state='disabled', bg='#DDA0DD', fg='black', disabledbackground='#DDA0DD', disabledforeground='black')
Oxidiser_Relief_Pressure_entry.grid(row=9, column=3, padx=5, pady=5)

##########################################################################################
#################################### Execution Button ####################################
##########################################################################################
Execute_Container = ttk.Frame(root, relief=tk.RAISED, borderwidth=2)
Execute_Container.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

Execute = ttk.Frame(Execute_Container, padding="5")
Execute.pack(fill="both", expand=True)

Execute.grid_columnconfigure(0, weight=1)
Execute.grid_columnconfigure(1, weight=1)
Execute.grid_columnconfigure(2, weight=6)
Execute.grid_rowconfigure(0, weight=1)
Execute.grid_rowconfigure(1, weight=1)
Execute.grid_rowconfigure(2, weight=1)

Execute_label = ttk.Label(Execute, text="Update/Export Values", font=("Arial", 14), anchor="center")
Execute_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

Export_unit_label = ttk.Label(Execute, text="Export Units:")
Export_unit_label.grid(row=2, column=0,  padx=5, pady=5, sticky="news")
button = ttk.Combobox(Execute, textvariable=Export_units, values=["in", "mm"], state="readonly", width=5)
button.grid(row=2, column=1, padx=5, pady=5)

button = ttk.Button(Execute, text="Update", command=update_all)
button.grid(row=1, column=2, padx=5, pady=5, sticky="news")

button = ttk.Button(Execute, text="Export to Excel", command=export_to_excel)
button.grid(row=2, column=2, padx=5, pady=5, sticky="news")


## Auto-executes

fuel_density_entry.bind('<KeyRelease>', update_all)
oxidiser_density_entry.bind('<KeyRelease>', update_all)

fuel_mass_flow_entry.bind('<KeyRelease>', update_all)
oxidiser_mass_flow_entry.bind('<KeyRelease>', update_all)

fuel_vehicle_diameter_entry.bind('<KeyRelease>', update_all)
oxidiser_vehicle_diameter_entry.bind('<KeyRelease>', update_all)

fuel_MEOP_entry.bind('<KeyRelease>', update_all)
oxidiser_MEOP_entry.bind('<KeyRelease>', update_all)

fuel_weld_eff_entry.bind('<KeyRelease>', update_all)
oxidiser_weld_eff_entry.bind('<KeyRelease>', update_all)

fuel_run_time_entry.bind('<KeyRelease>', update_all)
oxidiser_run_time_entry.bind('<KeyRelease>', update_all)

fuel_ullage_entry.bind('<KeyRelease>', update_all)
oxidiser_ullage_entry.bind('<KeyRelease>', update_all)

S_fuel_entry.bind('<KeyRelease>', update_all)
S_oxidiser_entry.bind('<KeyRelease>', update_all)

Fuel_Cap_Skirt_Length_entry.bind('<KeyRelease>', update_all)
Oxidiser_Cap_Skirt_Length_entry.bind('<KeyRelease>', update_all)

Fuel_Cap_Outlet_Ports_entry.bind('<KeyRelease>', on_fuel_outlet_ports_change)
Oxidiser_Cap_Outlet_Ports_entry.bind('<KeyRelease>', on_oxidiser_outlet_ports_change)

Fuel_Cap_Inlet_Ports_entry.bind('<KeyRelease>', on_fuel_inlet_ports_change)
Oxidiser_Cap_Inlet_Ports_entry.bind('<KeyRelease>', on_oxidiser_inlet_ports_change)


root.mainloop()



