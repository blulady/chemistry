''' The program is designed to solve non-graphic problems in a first year general chemistry book.
There are three environments. In the laboratory environment, anything can be created or 'deconstructed'
and each step of the process should be recorded and displayed to verify the process and to aid a student
learning general chemistry.
The industrial and nature environments only describes industrial and natural processes.
There is no experimentation in these environments and the level of detail in explanations varies.
The main part of the program is the laboratory process in which a process is selected, all the appropriate field
values are entered, calculations are made, results are presented, and a record of the process is stored. Later,
that record can be retrieved and used to recreate the process for verification and learning.
The ideal is that every important aspect of each process should be described and explained.
Especially, each step in the process, the equipment and energy used, the side effects and by-products.
'''
import sys
from tkinter import *  # get widget classes
from tkinter.ttk import Combobox, Entry, Label
#import ttk
import logging
logging.basicConfig(
    filename = 'app.log',            # Name of the log file (omit to use stderr)
    filemode = 'w',                  # File mode (use 'a' to append)
    level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
)
import tkinter as tk
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import *
from scipy import constants
from sqlite3 import *
#from sqlite3 import Error
import pdb
from tkinter import messagebox as mb #*  # get standard dialogs
#from MessageBoxes import *
from tkinter import messagebox as mb
from tkinter import font
#from ElementsDict import *
# import SQL_tables_to_dict_str
#from eci_dicts_lists import *
from CompoundsDict import *
from ionDict import *
from eciDict import *
#from ConVarFunEtc import *
from collections import defaultdict
#import defaultdict

root = Tk()
root.geometry("1800x800")
titlefont = ('Ariel', 14, 'bold')
labelfont = ('Ariel', 14)  # , 'bold')
buttonfont = ('Ariel', 12)  # , 'bold')
entryfont = ('Ariel', 12)  # , 'bold')

# Use the following structure to create frames and a canvas and scrollbar
# in order to attach the scrollbar to the canvas
#Create a Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand = 1)
#Create a Canvas
main_canvas = Canvas(main_frame)
main_canvas.pack(side=LEFT, fill=BOTH, expand = 1)
# Add a Scrollbar to the Canvas
sb = Scrollbar(main_frame, orient=VERTICAL,command=main_canvas.yview)
sb.pack(side=RIGHT, fill=Y)
# Configure the Canvas
main_canvas.configure(yscrollcommand=sb.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))
# Create another Frame inside the Canvas
inside_frame = Frame(main_canvas)
# Add the new froma to a Window in the Canvas
main_canvas.create_window((0,0), window = inside_frame, anchor = "nw")

''' Create additional windows for instructions and Calculations and Conversions'''
winInstructions = Toplevel()
e_Instructions = Text(winInstructions, height=20, width=50)
e_Instructions.grid(row=0, column=0) #, columnspan=6, sticky=W)
e_Instructions.config(font=entryfont)
e_Instructions.insert(END, "Program instructions will be provided in this window. \n")
e_Instructions.insert(END, "Move this window so it is always visible, or minimize it are resize it as needed. \n")
e_Instructions.insert(END, "Process instructions will be provided in this window. \n")

def Calculate():
    #print("Calculate is not yet functional. \n")
    e_Calculate.insert(END, "Calculate is not yet functional. \n")

''' The following create the window winCalculate. 
    This window is used to perform unit conversions and other calculations. '''
winCalculate = Toplevel()
#from scipy import constants
constants.value(u'elementary charge')
print(constants.value(u'elementary charge'))
''' Entry and CB variables follow. '''
unit_values = "kilogram gram kilometer meter day hour minute second mile yard foot inch K F C ampere volt ohm candela mole pound ounce"
cb_process_values = "equals conversion addition subtraction multiplication division power s_root"

e_1_qty = DoubleVar(0)
e_2_qty = DoubleVar(0)
e_2a_qty = DoubleVar(0)
e_3_qty = DoubleVar(0)
e_3a_qty = DoubleVar(0)
e_4_qty = DoubleVar(0)
eci_1_units = StringVar()
eci_1a_units = StringVar()
eci_2_units = StringVar()
eci_2a_units = StringVar()
eci_3_units = StringVar()
eci_3a_units = StringVar()
eci_4_units = StringVar()
eci_4a_units = StringVar()
eci_1_process = StringVar()
eci_2_process = StringVar()
eci_3_process = StringVar()

''' End of Entry and CB variable definitions. '''
# Imponts u as 1.602176634e-19
lbl_Title = Label(winCalculate, text="Calculations and Conversions")
lbl_Title.grid(row=0, column=0, columnspan=6, sticky=W)
lbl_Title.config(font=titlefont)
lbl_blank = Label(winCalculate, text="")
lbl_blank.grid(row=1, column=0)
lbl_blank.config(font=labelfont)
btn_calculate = Button(winCalculate, text="Calculate", command=Calculate)
btn_calculate.grid(row=1, column=3)
btn_calculate.config(font=buttonfont)
#btn_continue.bind("<<ComboboxSelected>>", Continue)
lbl_eci_1N = Label(winCalculate, text="Number", width=8)
lbl_eci_1N.grid(row=2, column=0)
lbl_eci_1N.config(font=labelfont)
#lbl_eci_1_units = Label(winCalculate, text="Exponent", width=10)
#lbl_eci_1_units.grid(row=2, column=1, sticky=W)
#lbl_eci_1_units.config(font=labelfont)
lbl_eci_1U = Label(winCalculate, text="Units", width=10)
lbl_eci_1U.grid(row=2, column=1, sticky=W)
lbl_eci_1U.config(font=labelfont)
lbl_eci_1P = Label(winCalculate, text="Process", width=10)
lbl_eci_1P.grid(row=2, column=2, sticky=W)
lbl_eci_1P.config(font=labelfont)
lbl_eci_2N = Label(winCalculate, text="Number", width=10)
lbl_eci_2N.grid(row=2, column=3, sticky=W)
lbl_eci_2N.config(font=labelfont)
lbl_eci_2U = Label(winCalculate, text="Units", width=10)
lbl_eci_2U.grid(row=2, column=4, sticky=W)
lbl_eci_2U.config(font=labelfont)
lbl_eci_2P = Label(winCalculate, text="Process", width=10)
lbl_eci_2P.grid(row=2, column=5, sticky=W)
lbl_eci_2P.config(font=labelfont)
lbl_eci_3N = Label(winCalculate, text="Number", width=10)
lbl_eci_3N.grid(row=2, column=6, sticky=W)
lbl_eci_3N.config(font=labelfont)
lbl_eci_3U = Label(winCalculate, text="Units", width=10)
lbl_eci_3U.grid(row=2, column=7, sticky=W)
lbl_eci_3U.config(font=labelfont)
lbl_eci_3P = Label(winCalculate, text="Process", width=10)
lbl_eci_3P.grid(row=2, column=8, sticky=W)
lbl_eci_3P.config(font=labelfont)
lbl_eci_4N = Label(winCalculate, text="Number", width=10)
lbl_eci_4N.grid(row=2, column=9, sticky=W)
lbl_eci_4N.config(font=labelfont)
lbl_eci_4U = Label(winCalculate, text="Units", width=10)
lbl_eci_4U.grid(row=2, column=10, sticky=W)
lbl_eci_4U.config(font=labelfont)
e_1_number = Entry(winCalculate, text="", textvariable=e_1_qty, width=8)
e_1_number.grid(row=3, column=0)
e_1_number.config(font=entryfont)
#e_1_exp = StringVar()
#e_1_exponent = Entry(winCalculate, text="", textvariable=e_1_exp, width=8)
#e_1_exponent.grid(row=3, column=1)
#e_1_exponent.config(font=entryfont)

cb_eci_1_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_1_units, width=10)
cb_eci_1_units.grid(row=3, column=1)
cb_eci_1_units.config(font=entryfont)
cb_1_process: Combobox = Combobox(winCalculate, values=cb_process_values, textvariable=eci_1_process, width=10)
cb_1_process.grid(row=3, column=2)
cb_1_process.config(font=entryfont)
e_2_number = Entry(winCalculate, text="", textvariable=e_2_qty, width=8)
e_2_number.grid(row=3, column=3)
e_2_number.config(font=entryfont)
cb_eci_2_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_2_units, width=10)
cb_eci_2_units.grid(row=3, column=4)
cb_eci_2_units.config(font=entryfont)
cb_eci_2_process: Combobox = Combobox(winCalculate, values=cb_process_values, textvariable=eci_2_process, width=10)
cb_eci_2_process.grid(row=3, column=5)
cb_eci_2_process.config(font=entryfont)
e_3_number = Entry(winCalculate, text="", textvariable=e_3_qty, width=8)
e_3_number.grid(row=3, column=6)
e_3_number.config(font=entryfont)
unit_values = "kilogram gram kilometer meter day hour minute second mile yard foot inch K F C ampere volt ohm candela mole pound ounce"
cb_eci_3_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_3_units, width=10)
cb_eci_3_units.grid(row=3, column=7)
cb_eci_3_units.config(font=entryfont)
cb_eci_3_process: Combobox = Combobox(winCalculate, values=cb_process_values, textvariable=eci_3_process, width=10)
cb_eci_3_process.grid(row=3, column=8)
cb_eci_3_process.config(font=entryfont)
e_4_number = Entry(winCalculate, text="", textvariable=e_4_qty, width=8)
e_4_number.grid(row=3, column=9)
e_4_number.config(font=entryfont)
cb_eci_4_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_4_units, width=10)
cb_eci_4_units.grid(row=3, column=10)
cb_eci_4_units.config(font=entryfont)
e_2a_number = Entry(winCalculate, text="", textvariable=e_2a_qty, width=8)
e_2a_number.grid(row=4, column=3)
e_2a_number.config(font=entryfont)
cb_eci_1a_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_1a_units, width=10)
cb_eci_1a_units.grid(row=4, column=1)
cb_eci_1a_units.config(font=entryfont)
cb_eci_2a_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_2a_units, width=10)
cb_eci_2a_units.grid(row=4, column=4)
cb_eci_2a_units.config(font=entryfont)
e_3a_number = Entry(winCalculate, text="", textvariable=e_3a_qty, width=8)
e_3a_number.grid(row=4, column=6)
e_3a_number.config(font=entryfont)
cb_eci_3a_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_3a_units, width=10)
cb_eci_3a_units.grid(row=4, column=7)
cb_eci_3a_units.config(font=entryfont)
cb_eci_4a_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_4a_units, width=10)
cb_eci_4a_units.grid(row=4, column=10)
cb_eci_4a_units.config(font=entryfont)
#cb_eci_1_units.bind("<<ComboboxSelected>>", eci_units_selected)
lbl_blank = Label(winCalculate, text="")
lbl_blank.grid(row=5, column=0)
lbl_blank.config(font=labelfont)
e_Calculate = Text(winCalculate, height=10, width=80)
e_Calculate.grid(row=6, column=0, columnspan=6, sticky=W)
e_Calculate.config(font=entryfont)
''' End of winCalculate form GUI creation. '''

''' Add variables from ConVarFunEtc until I can find and fix the error. '''
'''Not all the elements and their attributes have been added to the database. H\u2082 works for H2 subscript'''
''' The following are not lists, but have list in the title because the string lists the items.'''
element_symbol_string = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br ' \
                        'Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er ' \
                        'Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Bi Po At Rn Fr Ra Ac Th Pa U Np Am Cm Bk Cf Es Fm Md No Lr ' \
                        'RF Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og'
element_name_string = 'Hydrogen Helium Lithium Beryllium Boron Carbon Nitrogen Oxygen Fluorine Neon Sodium Magnesium Aluminum ' \
                      'Silicon Phosphorus Sulfur Chlorine Argon Potassium Calcium Scandium Lead Vanadium Chromium Manganese Iron ' \
                      'Cobalt Nickel Copper Zinc Gallium Germanium Arsenic Selenium Bromine Krypton Rubidium Strontium Yttrium ' \
                      'Zirconium Niobium Molybdenum Technetium Ruthenium Rhodium Palladium Silver Cadmium Indium Tin Antimony ' \
                      'Tellurium Iodine Xenon Cesium Barium Lanthanium Cerium Praseodymium Neodynium Promethium Samarium Europium ' \
                      'Gadolinium Terbium Dysprosium Holmium Erbium Thulium Ytterbium Lutetium Hafnium Tantalum Tungsten Rhenium ' \
                      'Osmium Iridium Platinum Gold Mercury Thallium Bismuth Polonium Astatine Radon Francium Radium Actinium ' \
                      'Thorium Plutonium Uranium Neptunium Americium Curium Berkelium Californium Einsteinium Fermium Mendelevium ' \
                      'Nobelium Lawrencium Ruthorfordium Dudmium Seaborgium Bohrium Hassium Meitnerium Darmstadtium Roentgenium ' \
                      'Copernicium Nihonium Flerovium Moscovium Livermorium Tennessine Oganesson'

''' This list of elements and names will help retrieve names from symbols. '''
# element = zip(elements_symbols_list, elements_name_list)
element_names_Dict = {'Hydrogen': 'H', 'Helium': 'He', 'Lithium': 'Li', 'Beryllium': 'Be', 'Boron': 'B', 'Carbon': 'C', 'Nitrogen': 'N',
                      'Oxygen': 'O', 'Fluorine': 'F', 'Neon': 'Ne', 'Sodium': 'Na', 'Magnesium': 'Mg', 'Aluminum': 'Al', 'Silicon': 'Si',
                      'Phosphorus': 'P', 'Sulfur': 'S', 'Chlorine': 'Cl', 'Argon': 'Ar', 'Potassium': 'K', 'Calcium': 'Ca', 'Scandium': 'Sc',
                      'Titanium': 'Ti', 'Vanadium': 'V', 'Chromium': 'Cr', 'Manganese': 'Mn', 'Iron': 'Fe', 'Cobalt': 'Co', 'Nickel': 'Ni',
                      'Copper': 'Cu', 'Zinc': 'Zn', 'Gallium': 'Ga', 'Germanium': 'Ge', 'Arsenic': 'As', 'Selenium': 'Se', 'Bromine': 'Br',
                      'Krypton': 'Kr', 'Rubidium': 'Rb', 'Strontium': 'Sr', 'Yttrium': 'Y', 'Zirconium': 'Zr', 'Niobium': 'Nb',
                      'Molybdenum': 'Mo', 'Technetium': 'Tc', 'Ruthenium': 'Ru', 'Rhodium': 'Rh', 'Palladium': 'Pd', 'Silver': 'Ag',
                      'Cadmium': 'Cd', 'Indium': 'In', 'Tin': 'Sn', 'Antimony': 'Sb', 'Tellurium': 'Te', 'Iodine': 'I', 'Xenon': 'Xe',
                      'Cesium': 'Cs', 'Barium': 'Ba', 'Lanthanium': 'La', 'Cerium': 'Ce', 'Praseodymium': 'Pr', 'Neodynium': 'Nd',
                      'Promethium': 'Pm', 'Samarium': 'Sm', 'Europium': 'Eu', 'Gadolinium': 'Gd', 'Terbium': 'Tb', 'Dysprosium': 'Dy',
                      'Holmium': 'Ho', 'Erbium': 'Er', 'Thulium': 'Tm', 'Ytterbium': 'Yb', 'Lutetium': 'Lu', 'Hafnium': 'Hf', 'Tantalum': 'Ta',
                      'Tungsten': 'W', 'Rhenium': 'Re', 'Osmium': 'Os', 'Iridium': 'Ir', 'Platinum': 'Pt', 'Gold': 'Au', 'Mercury': 'Hg',
                      'Thallium': 'Tl', 'Lead': 'Ti', 'Bismuth': 'Bi', 'Polonium': 'Po', 'Astatine': 'At', 'Radon': 'Rn', 'Francium': 'Fr',
                      'Radium': 'Ra', 'Actinium': 'Ac', 'Thorium': 'Th', 'Protactinium': 'Pa', 'Uranium': 'U', 'Neptunium': 'Np',
                      'Plutonium': 'Pa', 'Americium': 'Am', 'Curium': 'Cm', 'Berkelium': 'Bk', 'Californium': 'Cf', 'Einsteinium': 'Es',
                      'Fermium': 'Fm', 'Mendelevium': 'Md', 'Nobelium': 'No', 'Lawrencium': 'Lr', 'Ruthorfordium': 'RF', 'Dudmium': 'Db',
                      'Seaborgium': 'Sg', 'Bohrium': 'Bh', 'Hassium': 'Hs', 'Meitnerium': 'Mt', 'Darmstadtium': 'Ds', 'Roentgenium': 'Rg',
                      'Copernicium': 'Cn', 'Nihonium': 'Nh', 'Flerovium': 'Fl', 'Moscovium': 'Mc', 'Livermorium': 'Lv', 'Tennessine': 'Ts',
                      'Oganesson': 'Og'}
''' Tried to change symbols to use subscripts, but the Compound Dictionary would not accept 
a subscripted formula as a valid key'''
compound_formula_string =  "Al4C3 AlCl3 Ar2He2Kr2Ne2Xe2Rn2 BCl3 Ca(H2PO4)2 CaI Ca(OH)2 Ca3P2 CdS CsF C6H8O7 CH3CO2H C2H3OOH" \
                           " CO CO2 HBr HC2H3O2 HCl HClO4 HCN H2CO3 HF HI HNO2 HNO3 H3PO4 H2S H2SO3 H2SO4 IF7 KBr KOH LiCl" \
                           " Mg3N2 NaCl NaHCO33 Na2O NaOH NH3 N2H4 NO NO2 N2O4 N2O N2O5 PF5 SO2 SO3 CH4 C2H6 C3H8 C4H10 C4H10_M" \
                           " C5H12 C6H14 C7H16 C8H18 C9H20 C10H22 C14H30 C18H38"

compound_name_string = "aluminum_carbide aluminum_chloride air boron_trichloride calcium_dihydrogen_phosphate calcium_iodide" \
                       " calcium_hydroxide calcium_phosphide cadmium_sulfide cesium_fluoride citric_acid acetic_acid acetic_acid" \
                       " carbon_monoxide carbon_dioxide hydrobromic_acid acetic_acid hydrochloric_acid perchloric_acid" \
                       " hydrogen_cyanide carbonic_acid hydrofluoric_acid hydroiodic_acid nitrous_acid nitric_acid" \
                       " phosphoric_acid hydrosulfuric_acid sulfurous_acid sulfuric_acid iodine_heptafluoride potassium_bromide" \
                       " potassium_hydroxide lithium_chloride magnesium_nitride sodium_chloride bicarbonate_of_soda sodium_oxide" \
                       " sodium_hydroxide ammonia hydrazine nitric_oxide nitorgen_dioxide dinitrogen_tetroxide nitrous_oxide" \
                       " dinitrogen_pentoxide phosphorus_pentafluoride sulfur_dioxide sulfur_trioxide methane ethane propane" \
                       " butane 2-methylpropane pentane hexane heptane octane nonane decane tetradecane octadecane"
''' This list of compounds and names will help retrieve names from formulas. Doesn't work. Why? '''
compounds_formula_dict = {'Al4C3': 'aluminum_carbide', 'AlCl3': 'aluminum_chloride', 'Ar2He2Kr2Ne2Xe2Rn2': 'air',
                        'BCl3': 'boron_trichloride', 'Ca(H2PO4)2': 'calcium_dihydrogen_phosphate', 'CaI': 'calcium_iodide',
                        'Ca(OH)2': 'calcium_hydroxide', 'Ca3P2': 'calcium_phosphide', 'CdS': 'cadmium_sulfide',
                        'CsF': 'cesium_fluoride', 'C6H8O7': 'citric_acid', 'CH3CO2H': 'acetic_acid', 'C2H3OOH': 'acetic_acid',
                        'CO': 'carbon_monoxide', 'CO2': 'carbon_dioxide', 'HBr': 'hydrobromic_acid', 'HC2H3O2': 'acetic_acid',
                        'HCl': 'hydrochloric_acid', 'HClO4': 'perchloric_acid', 'HCN': 'hydrogen_cyanide',
                        'H2CO3': 'carbonic_acid', 'HF': 'hydrofluoric_acid', 'HI': 'hydroiodic_acid', 'HNO2': 'nitrous_acid',
                        'HNO3': 'nitric_acid', 'H3PO4': 'phosphoric_acid', 'H2S': 'hydrosulfuric_acid', 'H2SO3': 'sulfurous_acid',
                        'H2SO4': 'sulfuric_acid', 'IF7': 'iodine_heptafluoride', 'KBr': 'potassium_bromide',
                        'KOH': 'potassium_hydroxide', 'LiCl': 'lithium_chloride', 'Mg3N2': 'magnesium_nitride',
                        'NaCl': 'sodium_chloride', 'NaHCO33': 'bicarbonate_of_soda', 'Na2O': 'sodium_oxide',
                        'NaOH': 'sodium_hydroxide', 'NH3': 'ammonia', 'N2H4': 'hydrazine', 'NO': 'nitric_oxide',
                        'NO2': 'nitorgen_dioxide', 'N2O4': 'dinitrogen_tetroxide', 'N2O': 'nitrous_oxide',
                        'N2O5': 'dinitrogen_pentoxide', 'PF5': 'phosphorus_pentafluoride', 'SO2': 'sulfur_dioxide',
                        'SO3': 'sulfur_trioxide', 'CH4': 'methane', 'C2H6': 'ethane', 'C3H8': 'propane', 'C4H10': 'butane',
                        'C4H10_M': '2-methylpropane', 'C5H12': 'pentane', 'C6H14': 'hexane', 'C7H16': 'heptane',
                        'C8H18': 'octane', 'C9H20': 'nonane', 'C10H22': 'decane', 'C14H30': 'tetradecane', 'C18H38': 'octadecane'}
compound_names_dict =  {'aluminum_carbide': 'Al4C3', 'aluminum_chloride': 'AlCl3', 'air': 'Ar2He2Kr2Ne2Xe2Rn2',
                        'boron_trichloride': 'BCl3', 'calcium_dihydrogen_phosphate': 'Ca(H2PO4)2', 'calcium_iodide': 'CaI',
                        'calcium_hydroxide': 'Ca(OH)2', 'calcium_phosphide': 'Ca3P2', 'cadmium_sulfide': 'CdS',
                        'cesium_fluoride': 'CsF', 'citric_acid': 'C6H8O7', 'acetic_acid': 'HC2H3O2', 'carbon_monoxide': 'CO',
                        'carbon_dioxide': 'CO2', 'hydrobromic_acid': 'HBr', 'hydrochloric_acid': 'HCl', 'perchloric_acid': 'HClO4',
                        'hydrogen_cyanide': 'HCN', 'carbonic_acid': 'H2CO3', 'hydrofluoric_acid': 'HF',
                        'hydroiodic_acid': 'HI', 'nitrous_acid': 'HNO2', 'nitric_acid': 'HNO3', 'phosphoric_acid': 'H3PO4',
                        'hydrosulfuric_acid': 'H2S', 'sulfurous_acid': 'H2SO3', 'sulfuric_acid': 'H2SO4',
                        'iodine_heptafluoride': 'IF7', 'potassium_bromide': 'KBr', 'potassium_hydroxide': 'KOH',
                        'lithium_chloride': 'LiCl', 'magnesium_nitride': 'Mg3N2', 'sodium_chloride': 'NaCl',
                        'bicarbonate_of_soda': 'NaHCO33', 'sodium_oxide': 'Na2O', 'sodium_hydroxide': 'NaOH',
                        'ammonia': 'NH3', 'hydrazine': 'N2H4', 'nitric_oxide': 'NO', 'nitorgen_dioxide': 'NO2',
                        'dinitrogen_tetroxide': 'N2O4', 'nitrous_oxide': 'N2O', 'dinitrogen_pentoxide': 'N2O5',
                        'phosphorus_pentafluoride': 'PF5', 'sulfur_dioxide': 'SO2', 'sulfur_trioxide': 'SO3', 'methane': 'CH4',
                        'ethane': 'C2H6', 'propane': 'C3H8', 'butane': 'C4H10', '2-methylpropane': 'C4H10_M', 'pentane': 'C5H12',
                        'hexane': 'C6H14', 'heptane': 'C7H16', 'octane': 'C8H18', 'nonane': 'C9H20', 'decane': 'C10H22',
                        'tetradecane': 'C14H30', 'octadecane': 'C18H38'}


ionic_compounds_symbols_string = "No list yet"
ionic_compounds_names_string = "No list yet"
''' An initial list of ions and names to fill the combo boxes until a proper list can be made. '''
ion_symbols_list = "C2H3O2 ClO2 ClO3 ClO4 CN CO32 CuS FeCl2 FeCl3 H2PO4 HCO3 Hg2O HgO H3O HPO42 HSO4 OH NH4 NO3 NO2 MnO4 O22 SO42 SO32 PO43"
ion_names_list = "acetate chlorite chlorate perchlorate cyanide carbonate copper_(II)_sulfide " \
                 "iron_(II)_chloride iron_(III)_chloride dihydrogen_phosphate hydrogen_carbonate " \
                 "mercury_(I)_oxide mercury_(II)_oxide hydronium hydrogen_phosphate hydrogen_sulfate " \
                 "hydroxide ammonium nitrate nitrite permanganate peroxide sulfate sulfite phosphate "

ion_names_dict = {'acetate': 'C2H3O2', 'chlorite': 'ClO2', 'chlorate': 'ClO3', 'perchlorate': 'ClO4',
                  'cyanide': 'CN', 'carbonate': 'CO32', 'copper_(II)_sulfide': 'CuS', 'iron_(II)_chloride': 'FeCl2',
                  'iron_(III)_chloride': 'FeCl3', 'dihydrogen_phosphate': 'H2PO4', 'hydrogen_carbonate': 'HCO3',
                  'mercury_(I)_oxide': 'Hg2O', 'mercury_(II)_oxide': 'HgO', 'hydronium': 'H3O',
                  'hydrogen_phosphate': 'HPO42', 'hydrogen_sulfate': 'HSO4', 'hydroxide': 'OH',
                  'ammonium': 'NH4', 'nitrate': 'NO3', 'nitrite': 'NO2',
                  'permanganate': 'MnO4', 'peroxide': 'H2O22', 'sulfate': 'SO42',
                  'sulfite': 'SO32', 'phosphate': 'PO43'}
polyatomic_formula_string = 'H2 N2 F2 O2 I2 Cl2 S8 Se8 P4 Br2'
polyatomic_name_string = 'Hydrogen Nitrogen Fluorine Oxygen Iodine Chlorine Sulfur Selenium Phosphorous Bromine'
''' Other variables used by Chemistry and other programs '''
''' combobox lists go here. Other variables go elsewhere. '''
unit_values = "Moles grams kilograms ounces pounds liters(l) liters(g) ml(l) ml(g)"
eci_cb_values = "elements compounds ionic_compounds ions acids bases polyatomic"
environment = "Laboratory Industry Nature"
temp_units = "K F C"
press_units = "ATM torr psi mmHg"

major_process_list = "Calculate Synthesis Decompostion Combustion Single_Replacement Double_Replacement Neutralization Precipitation Balance_Equation Set_default_T_and_P Parse_Reactants Parse_Products Acid_Base Oxidation_Reduction Oxidation_Rate Metathesis Refinement"
minor_process_list = "Set_STP_Variables Pressure Volume, moles Temperature pvnrt "
equipment = "refinery blah1 blah2"
energy_type = "heat electricity"
catalyst = "blah1 blah2 blah3 blah4"
side_effects = "air_polution water_polution land_polution"
by_products = "CO CO2 NO NO2"
variables = "Av Bv Cv Kv"  # Variable names cannot conflict with element symbols like B C H K etc
''' Variables to hold the selected items of combo boxes. '''
major_process_selected = ""
minor_process_selected = ""
equipment_selected = ""
energy_type_selected = ""
catalyst_selected = ""
side_effect_selected = ""
by_product_selected = ""
variable_selected = ""
variable_value = DoubleVar()
Init_default_T_and_P = FALSE
Av = DoubleVar()
Bv = DoubleVar()
Cv = DoubleVar()
Kv = DoubleVar()

''' Miscellaneous variables to use until proper variables are created. '''
valences = "7 6 5 4 3 2 1 0 -1 -2 -3 -4"


''' This list of elements and names will help retrieve names from symbols. '''
# element = zip(elements_symbols_list, elements_name_list)

''' Tried to change symbols to use subscripts, but the Compound Dictionary would not accept
a subscripted formula as a valid key'''

current_eci = ""
variable_value = "" #DoubleVar()
Init_default_T_and_P = FALSE
Av = "" #DoubleVar()
Bv = "" #DoubleVar()
Cv = "" #DoubleVar()
Kv = "" #DoubleVar()

#for i in range(40):
#    Button(inside_frame, text = f'Button {i}').grid(row=i, column=0)
''' Add lists here '''
dbr = {}
''' Define the record dictionary 
'''
r1 = dict(name= 'Record 1', id= 1, compound= 'None', process= 'None', major_process= 'None', minor_process= 'None', environment= 'None',
          equipment = "", energy_type = "", energy_amount = "", catalyst = "", side_effects = "", by_products = "",
          variables = "", variable_values = "", explanation = "",
          eci_1_type = "", eci_1_formula= "", eci_1_name = "", eci_1_units = "grams", eci_1_qty = "", eci_1_M_qty = "", eci_1_valence = "",
          eci_1_temp_display_units = "C", eci_1_temp_calc_units = "K", eci_1_temp_display_qty = "", eci_1_temp_calc_qty = "",
          eci_1_press_display_units = "atm", eci_1_press_calc_units = "atm", eci_1_press_display_qty = "", eci_1_press_calc_qty = "",
          eci_2_type = "", eci_2_formula= "", eci_2_name = "", eci_2_units = "grams", eci_2_qty = "", eci_2_M_qty = "", eci_2_valence = "",
          eci_2_temp_display_units = "C", eci_2_temp_calc_units = "K", eci_2_temp_display_qty = "", eci_2_temp_calc_qty = "",
          eci_2_press_display_units = "atm", eci_2_press_calc_units = "atm", eci_2_press_display_qty = "", eci_2_press_calc_qty = "",
          eci_3_type = "", eci_3_formula= "", eci_3_name = "", eci_3_units = "grams", eci_3_qty = "", eci_3_M_qty = "", eci_3_valence = "",
          eci_3_temp_display_units = "C", eci_3_temp_calc_units = "K", eci_3_temp_display_qty = "", eci_3_temp_calc_qty = "",
          eci_3_press_display_units = "atm", eci_3_press_calc_units = "atm", eci_3_press_display_qty = "", eci_3_press_calc_qty = "",
          eci_4_type = "", eci_4_formula= "", eci_4_name = "", eci_4_units = "grams", eci_4_qty = "", eci_4_M_qty = "", eci_4_valence = "",
          eci_4_temp_display_units = "C", eci_4_temp_calc_units = "K", eci_4_temp_display_qty = "", eci_4_temp_calc_qty = "",
          eci_4_press_display_units = "atm", eci_4_press_calc_units = "atm", eci_4_press_display_qty = "", eci_4_press_calc_qty = "",
          eci_5_type = "", eci_5_formula= "", eci_5_name = "", eci_5_units = "grams", eci_5_qty = "", eci_5_M_qty = "", eci_5_valence = "",
          eci_5_temp_display_units = "atm", eci_5_temp_calc_units = "K", eci_5_temp_display_qty = "", eci_5_temp_calc_qty = "",
          eci_5_press_display_units = "C", eci_5_press_calc_units = "atm", eci_5_press_display_qty = "", eci_5_press_calc_qty = "",
          eci_6_type = "", eci_6_formula= "atm", eci_6_name = "", eci_6_units = "grams", eci_6_qty = "", eci_6_M_qty = "", eci_6_valence = "",
          eci_6_temp_display_units = "C", eci_6_temp_calc_units = "K", eci_6_temp_display_qty = "", eci_6_temp_calc_qty = "",
          eci_6_press_display_units = "atm", eci_6_press_calc_units = "atm", eci_6_press_display_qty = "", eci_6_press_calc_qty = "",)

dbr['R1'] = r1
#def create_element_dict():, compound= 'None'
H = dict(id= 1, symbol= 'H', name= 'Hydrogen', atomic_number= 1, mass= 1.008, period= 1, row= 1, column= 1, _group= '1A 7A', protons= 1, neutrons= 0, electrons= 1, _1s= 1, _2s= 0, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-72', density= '0.00008988', electronegativity= '2.1', melt= '14.01', boil= '-252.76', e_fusion= 'ef', e_vapor= 'ev', t_crit= '-240.17', p_crit= '12.77', valence= '1 -1', a_radius= '53')
He = dict(id= 2, symbol= 'He', name= 'Helium', atomic_number= 2, mass= 4.002602, period= 1, row= 1, column= 18, _group= '8A', protons= 2, neutrons= 2, electrons= 2, _1s= 2, _2s= 0, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '20', density= '0.0001785', electronegativity= '0.0', melt= 'NULL', boil= '-268.94', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-267.9550', p_crit= '2.261', valence= '0', a_radius= '31')
Li = dict(id= 3, symbol= 'Li', name= 'Lithium', atomic_number= 3, mass= 6.941, period= 2, row= 2, column= 1, _group= '1A', protons= 3, neutrons= 3, electrons= 3, _1s= 2, _2s= 1, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-60', density= '0.535', electronegativity= '1.0', melt= '180.50', boil= '1342', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '2950', p_crit= '67', valence= '1', a_radius= '167')
Be = dict(id= 4, symbol= 'Be', name= 'Beryllium', atomic_number= 4, mass= 9.012182, period= 2, row= 2, column= 2, _group= '2A', protons= 4, neutrons= 4, electrons= 4, _1s= 2, _2s= 2, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '240', density= '1.848', electronegativity= '1.5', melt= '1287', boil= '2468', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '4932', p_crit= 'NULL', valence= '2', a_radius= '112')
B = dict(id= 5, symbol= 'B', name= 'Boron', atomic_number= 5, mass= 10.8111, period= 2, row= 2, column= 13, _group= '3A', protons= 5, neutrons= 5, electrons= 5, _1s= 2, _2s= 2, _2p= 1, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-23', density= '2.460', electronegativity= '2.0', melt= '2077', boil= '4000', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '3', a_radius= '87')
C = dict(id= 6, symbol= 'C', name= 'Carbon', atomic_number= 6, mass= 12.0107, period= 2, row= 2, column= 14, _group= '4A', protons= 6, neutrons= 6, electrons= 6, _1s= 2, _2s= 2, _2p= 2, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-123', density= '2.260', electronegativity= '2.5', melt= '4489', boil= '3825', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '4 3 2 1 0 -1 -2 -3 -4', a_radius= '67')
N = dict(id= 7, symbol= 'N', name= 'Nitrogen', atomic_number= 7, mass= 14.0087, period= 2, row= 2, column= 15, _group= '5A', protons= 7, neutrons= 7, electrons= 7, _1s= 2, _2s= 2, _2p= 3, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '0', density= '0.001251', electronegativity= '3.0', melt= '-210.0', boil= '-195.795', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-146.89', p_crit= '33.54', valence= '5 4 3 2 1 -1 -2 -3', a_radius= '56')
O = dict(id= 8, symbol= 'O', name= 'Oxygen', atomic_number= 8, mass= 15.9994, period= 2, row= 2, column= 16, _group= '6A', protons= 8, neutrons= 8, electrons= 8, _1s= 2, _2s= 2, _2p= 4, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-141', density= '0.001429', electronegativity= '3.5', melt= '-218.79', boil= '-182.962', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-118.38', p_crit= '50.14', valence= '-1 -2', a_radius= '48')
F = dict(id= 9, symbol= 'F', name= 'Fluorine', atomic_number= 9, mass= 18.9984032, period= 2, row= 2, column= 17, _group= '7A', protons= 9, neutrons= 9, electrons= 9, _1s= 2, _2s= 2, _2p= 5, _3s= 0, _3p= 1, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-322', density= '0.001696', electronegativity= '4.0', melt= '-219.67', boil= '-188.11', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-128.74', p_crit= '5.1724', valence= '-1', a_radius= '42')
Ne = dict(id= 10, symbol= 'Ne', name= 'Neon', atomic_number= 10, mass= 20.1797, period= 2, row= 2, column= 18, _group= '8A', protons= 10, neutrons= 10, electrons= 10, _1s= 2, _2s= 2, _2p= 6, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '30', density= '0.000900', electronegativity= '0.0', melt= '-248.59', boil= '-246.046', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-228.6580', p_crit= '26.86', valence= '0', a_radius= '38')
Na = dict(id= 11, symbol= 'Na', name= 'Sodium', atomic_number= 11, mass= 22.989770, period= 3, row= 3, column= 1, _group= '1A', protons= 11, neutrons= 11, electrons= 11, _1s= 2, _2s= 2, _2p= 6, _3s= 1, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-53', density= '0.968', electronegativity= '0.9', melt= '97.794', boil= '882.940', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '2300', p_crit= '35', valence= '1', a_radius= '190')
Mg = dict(id= 12, symbol= 'Mg', name= 'Magnesium', atomic_number= 12, mass= 24.3050, period= 3, row= 3, column= 2, _group= '2A', protons= 12, neutrons= 12, electrons= 12, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '230', density= '1.738', electronegativity= '1.2', melt= '650', boil= '1090', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '2', a_radius= '145')
Al = dict(id= 13, symbol= 'Al', name= 'Aluminum', atomic_number= 13, mass= 26.981538, period= 3, row= 3, column= 13, _group= '3A', protons= 13, neutrons= 13, electrons= 13, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 1, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-44', density= '2.7', electronegativity= '1.5', melt= '660.323', boil= '2519', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '6427', p_crit= 'NULL', valence= '3', a_radius= '118')
Si = dict(id= 14, symbol= 'Si', name= 'Silicon', atomic_number= 14, mass= '28.0855', period= 3, row= 3, column= 14, _group= '4A', protons= 14, neutrons= 14, electrons= 14, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 2, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-120', density= '2.330', electronegativity= '1.8', melt= '1414', boil= '3265', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '4', a_radius= '111')
P = dict(id= 15, symbol= 'P', name= 'Phosphorus', atomic_number= 15, mass= '30.973761', period= 3, row= 3, column= 15, _group= '5A, 7A', protons= 15, neutrons= 15, electrons= 15, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 3, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-74', density= '1.823', electronegativity= '2.1', melt= '44.15 579.2', boil= '280.5 431', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '721', p_crit= 'NULL', valence= '5 3 -3', a_radius= '98')
S = dict(id= 16, symbol= 'S', name= 'Sulfur', atomic_number= 16, mass= '32.065', period= 3, row= 3, column= 16, _group= '6A', protons= 16, neutrons= 16, electrons= 16, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 4, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-201', density= '1.960', electronegativity= '2.5', melt= '95.2 115.21', boil= '4461', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '1041', p_crit= 'NULL', valence= '6 4 -2', a_radius= '88')
Cl = dict(id= 17, symbol= 'Cl', name= 'Chlorine', atomic_number= 17, mass= '35.453', period= 3, row= 3, column= 17, _group= '7A', protons= 17, neutrons= 17, electrons= 17, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 5, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-348', density= '0.003214', electronegativity= '3.0', melt= '-101.5', boil= '-34.03', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '143.9', p_crit= '78.1', valence= '7 5 3 1 -1', a_radius= '79')
Ar = dict(id= 18, symbol= 'Ar', name= 'Argon', atomic_number= 18, mass= '39.948', period= 3, row= 3, column= 18, _group= '8A', protons= 18, neutrons= 18, electrons= 18, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '35', density= '0.001784', electronegativity= '0.0', melt= '-189.34', boil= '-185.854', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-122.463', p_crit= '4.863', valence= '0', a_radius= '71')
K = dict(id= 19, symbol= 'K', name= 'Potassium', atomic_number= 19, mass= '39.0983', period= 4, row= 4, column= 1, _group= '1A', protons= 19, neutrons= 19, electrons= 19, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 1, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-48', density= '0.856', electronegativity= '0.8', melt= '63.5', boil= '759', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '1950', p_crit= '16', valence= '1', a_radius= '243')
Ca = dict(id= 20, symbol= 'Ca', name= 'Calcium', atomic_number= 20, mass= '40.078', period= 4, row= 4, column= 2, _group= '2A', protons= 20, neutrons= 20, electrons= 20, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '150', density= '1.550', electronegativity= '1.0', melt= '842', boil= '1484', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '2', a_radius= '194')
Sc = dict(id= 21, symbol= 'Sc', name= 'Scandium', atomic_number= 21, mass= '44.955910', period= 4, row= 4, column= 3, _group= '3B', protons= 21, neutrons= 21, electrons= 21, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 1, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '2.985', electronegativity= '1.3', melt= '1541', boil= '2836', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '184')
Ti = dict(id= 22, symbol= 'Ti', name= 'Titanium', atomic_number= 22, mass= '47.867', period= 4, row= 4, column= 4, _group= '4B', protons= 22, neutrons= 22, electrons= 22, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 2, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '4.507', electronegativity= '1.5', melt= '1670', boil= '3287', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '176')
V = dict(id= 23, symbol= 'V', name= 'Vanadium', atomic_number= 23, mass= '50.9415', period= 4, row= 4, column= 5, _group= '5B', protons= 23, neutrons= 23, electrons= 23, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 3, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '6.110', electronegativity= '1.6', melt= '1910', boil= '3407', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '171')
Cr = dict(id= 24, symbol= 'Cr', name= 'Chromium', atomic_number= 24, mass= '51.9961', period= 4, row= 4, column= 6, _group= '6B', protons= 24, neutrons= 24, electrons= 24, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 1, _3d= 5, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '7.140', electronegativity= '1.6', melt= '1907', boil= '2671', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '166')
Mn = dict(id= 25, symbol= 'Mn', name= 'Manganese', atomic_number= 25, mass= '54.938049', period= 4, row= 4, column= 7, _group= '7B', protons= 25, neutrons= 25, electrons= 25, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 5, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '7.470', electronegativity= '1.5', melt= '1246', boil= '2061', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '4052', p_crit= 'NULL', valence= 'NULL', a_radius= '161')
Fe = dict(id= 26, symbol= 'Fe', name= 'Iron', atomic_number= 26, mass= '55.845', period= 4, row= 4, column= 8, _group= '8B', protons= 26, neutrons= 26, electrons= 26, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 6, _4p= 2, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '7.874', electronegativity= '1.8', melt= '1538', boil= '2861', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '9067', p_crit= 'NULL', valence= 'NULL', a_radius= '156')
Co = dict(id= 27, symbol= 'Co', name= 'Cobalt', atomic_number= 27, mass= '58.9932', period= 4, row= 4, column= 9, _group= '8B', protons= 27, neutrons= 27, electrons= 27, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 7, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.9', electronegativity= '1.9', melt= '1495', boil= '2927', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '152')
Ni = dict(id= 28, symbol= 'Ni', name= 'Nickel', atomic_number= 28, mass= '58.6934', period= 4, row= 4, column= 10, _group= '8B', protons= 28, neutrons= 28, electrons= 28, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 8, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.908', electronegativity= '1.9', melt= '1455', boil= '2913', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '149')
Cu = dict(id= 29, symbol= 'Cu', name= 'Copper', atomic_number= 29, mass= '63.546', period= 4, row= 4, column= 11, _group= '1B', protons= 29, neutrons= 29, electrons= 29, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 1, _3d= 10, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.920', electronegativity= '1.9', melt= '1084.62', boil= '2560', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '145')
Zn = dict(id= 30, symbol= 'Zn', name= 'Zinc', atomic_number= 30, mass= '65.409', period= 4, row= 4, column= 12, _group= '2B', protons= 30, neutrons= 30, electrons= 30, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '7.140', electronegativity= '1.6', melt= '419.527', boil= '907', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '2', a_radius= '142')
Ga = dict(id= 31, symbol= 'Ga', name= 'Gallium', atomic_number= 31, mass= '69.723', period= 4, row= 4, column= 13, _group= '3A', protons= 31, neutrons= 31, electrons= 31, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 1, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-40', density= '5.904', electronegativity= '1.6', melt= '29.7646', boil= '2229', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '3', a_radius= '136')
Ge = dict(id= 32, symbol= 'Ge', name= 'Germanium', atomic_number= 32, mass= '72.64', period= 4, row= 4, column= 14, _group= '4A', protons= 32, neutrons= 32, electrons= 32, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 2, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-116', density= '5.323', electronegativity= '1.8', melt= '938.25', boil= '2833', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '4', a_radius= '125')
As = dict(id= 33, symbol= 'As', name= 'Arsenic', atomic_number= 33, mass= '74.92160', period= 4, row= 4, column= 15, _group= '5A', protons= 33, neutrons= 33, electrons= 33, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 3, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-77', density= '5.727', electronegativity= '2.0', melt= '817', boil= '616', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '5 3 -3', a_radius= '114')
Se = dict(id= 34, symbol= 'Se', name= 'Selenium', atomic_number= 34, mass= '778.96', period= 4, row= 4, column= 16, _group= '6A', protons= 34, neutrons= 34, electrons= 34, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 4, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-195', density= '4.819', electronegativity= '2.4', melt= '220.8', boil= '685', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '6 4 -2', a_radius= '103')
Br = dict(id= 35, symbol= 'Br', name= 'Bromine', atomic_number= 35, mass= '79.904', period= 4, row= 4, column= 17, _group= '7A', protons= 35, neutrons= 35, electrons= 35, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 5, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-324', density= '3.120', electronegativity= '2.8', melt= '-7.2', boil= '58.8', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '7 5 3 1 -1', a_radius= '94')
Kr = dict(id= 36, symbol= 'Kr', name= 'Krypton', atomic_number= 36, mass= '83.798', period= 4, row= 4, column= 18, _group= '8A', protons= 36, neutrons= 36, electrons= 36, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '40', density= '0.00375', electronegativity= '0', melt= '-157.37', boil= '-153.415', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '4 2', a_radius= '88')
Rb = dict(id= 37, symbol= 'Rb', name= 'Rubidium', atomic_number= 37, mass= '85.4678', period= 5, row= 5, column= 1, _group= '1A', protons= 37, neutrons= 37, electrons= 37, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 0, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-46', density= '1.532', electronegativity= '0.8', melt= '39.30', boil= '688', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '1', a_radius= '265')
Sr = dict(id= 38, symbol= 'Sr', name= 'Strontium', atomic_number= 38, mass= '87.62', period= 5, row= 5, column= 2, _group= '2A', protons= 38, neutrons= 38, electrons= 38, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 0, _5s= 2, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '160', density= '2.630', electronegativity= '1.0', melt= '777', boil= '1377', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '2', a_radius= '219')
Y = dict(id= 39, symbol= 'Y', name= 'Yttrium', atomic_number= 39, mass= '88.90585', period= 5, row= 5, column= 3, _group= '3B', protons= 39, neutrons= 39, electrons= 30, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 1, _5s= 2, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '4.472', electronegativity= '1.2', melt= '1522', boil= '3345', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '212')
Zr = dict(id= 40, symbol= 'Zr', name= 'Zirconium', atomic_number= 40, mass= '91.224', period= 5, row= 5, column= 4, _group= '4B', protons= 40, neutrons= 40, electrons= 40, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 2, _5s= 2, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '6.511', electronegativity= '1.4', melt= '1854', boil= '4406', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '206')
Nb = dict(id= 41, symbol= 'Nb', name= 'Niobium', atomic_number= 41, mass= '92.90638', period= 5, row= 5, column= 5, _group= '5B', protons= 41, neutrons= 41, electrons= 41, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 4, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.570', electronegativity= '1.6', melt= '2477', boil= '4741', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '198')
Mo = dict(id= 42, symbol= 'Mo', name= 'Molybdenum', atomic_number= 42, mass= '95.94', period= 5, row= 5, column= 6, _group= '6B', protons= 42, neutrons= 42, electrons= 42, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 5, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '10.280', electronegativity= '1.8', melt= '2622', boil= '4639', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '190')
Tc = dict(id= 43, symbol= 'Tc', name= 'Technetium', atomic_number= 43, mass= '98', period= 5, row= 5, column= 7, _group= '7B', protons= 43, neutrons= 43, electrons= 43, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 6, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '11.5', electronegativity= '1.9', melt= '2157', boil= '4262', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '183')
Ru = dict(id= 44, symbol= 'Ru', name= 'Ruthenium', atomic_number= 44, mass= '101.07', period= 5, row= 5, column= 8, _group= '8B', protons= 44, neutrons= 44, electrons= 44, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 7, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '12.370', electronegativity= '2.2', melt= '2333', boil= '4147', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '178')
Rh = dict(id= 45, symbol= 'Rh', name= 'Rhodium', atomic_number= 45, mass= '102.90550', period= 5, row= 5, column= 9, _group= '8B', protons= 45, neutrons= 45, electrons= 45, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 8, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '12.450', electronegativity= '2.2', melt= '1963', boil= '3695', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '173')
Pd = dict(id= 46, symbol= 'Pd', name= 'Palladium', atomic_number= 46, mass= '106.42', period= 5, row= 5, column= 10, _group= '8B', protons= 46, neutrons= 46, electrons= 46, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '12.023', electronegativity= '2.2', melt= '1554.8', boil= '2963', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '169')
Ag = dict(id= 47, symbol= 'Ag', name= 'Silver', atomic_number= 47, mass= '107.8682', period= 5, row= 5, column= 11, _group= '1B', protons= 47, neutrons= 47, electrons= 47, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '10.490', electronegativity= '1.9', melt= '961.78', boil= '2162', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '6137', p_crit= 'Press Crit', valence= 'NULL', a_radius= '165')
Cd = dict(id= 48, symbol= 'Cd', name= 'Cadmium', atomic_number= 48, mass= '112.411', period= 5, row= 5, column= 12, _group= '2B', protons= 48, neutrons= 48, electrons= 48, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.650', electronegativity= '1.7', melt= '321.069', boil= '767', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '2', a_radius= '161')
La = dict(id= 57, symbol= 'La', name= 'Lanthanium', atomic_number= 57, mass= '138.90547', period= 6, row= 6, column= 3, _group= '19', protons= 57, neutrons= 82, electrons= 57, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _5d= 1, _6p= 0, _7s= 0, affinity= '40', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ce = dict(id= 58, symbol= 'Ce', name= 'Cerium', atomic_number= 58, mass= '140.166', period= 6, row= 6, column= 3, _group= '19', protons= 58, neutrons= 82, electrons= 58, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 1, _5d= 1, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Pr = dict(id= 59, symbol= 'Pr', name= 'Praseodymium', atomic_number= 59, mass= '140.907', period= 6, row= 6, column= 3, _group= '19', protons= 59, neutrons= 82, electrons= 59, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 3, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Nd = dict(id= 60, symbol= 'Nd', name= 'Neodynium', atomic_number= 60, mass= '144.242', period= 6, row= 6, column= 3, _group= '19', protons= 60, neutrons= 84, electrons= 60, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 4, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '1010.0', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Pm = dict(id= 61, symbol= 'Pm', name= 'Promethium', atomic_number= 61, mass= '145', period= 6, row= 6, column= 3, _group= '19', protons= 61, neutrons= 84, electrons= 61, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 5, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Sm = dict(id= 62, symbol= 'Sm', name= 'Samarium', atomic_number= 62, mass= '150.36', period= 6, row= 6, column= 3, _group= '19', protons= 62, neutrons= 88, electrons= 62, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 6, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Eu = dict(id= 63, symbol= 'Eu', name= 'Europium', atomic_number= 63, mass= '151.964', period= 6, row= 6, column= 3, _group= '19', protons= 63, neutrons= 89, electrons= 63, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 7, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '822.0', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Gd = dict(id= 64, symbol= 'Gd', name= 'Gadolinium', atomic_number= 64, mass= '157.25', period= 6, row= 6, column= 3, _group= '19', protons= 64, neutrons= 93, electrons= 64, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 7, _5d= 1, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Tb = dict(id= 65, symbol= 'Tb', name= 'Terbium', atomic_number= 65, mass= '158.92535', period= 6, row= 6, column= 3, _group= '19', protons= 65, neutrons= 94, electrons= 65, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 9, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Dy = dict(id= 66, symbol= 'Dy', name= 'Dysprosium', atomic_number= 66, mass= '162.500', period= 6, row= 6, column= 3, _group= '19', protons= 66, neutrons= 97, electrons= 66, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 10, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ho = dict(id= 67, symbol= 'Ho', name= 'Holmium', atomic_number= 67, mass= '164.93033', period= 6, row= 6, column= 3, _group= '19', protons= 67, neutrons= 98, electrons= 67, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 11, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Er = dict(id= 68, symbol= 'Er', name= 'Erbium', atomic_number= 68, mass= '167.259', period= 6, row= 6, column= 3, _group= '19', protons= 68, neutrons= 99, electrons= 68, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 12, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Tm = dict(id= 69, symbol= 'Tm', name= 'Thulium', atomic_number= 69, mass= '168.93422', period= 6, row= 6, column= 3, _group= '19', protons= 69, neutrons= 100, electrons= 69, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 13, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Yb = dict(id= 70, symbol= 'Yb', name= 'Ytterbium', atomic_number= 70, mass= '173.054', period= 6, row= 6, column= 3, _group= '19', protons= 70, neutrons= 103, electrons= 70, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Lu = dict(id= 71, symbol= 'Lu', name= 'Lutetium', atomic_number= 71, mass= '174.9668', period= 6, row= 6, column= 3, _group= '19', protons= 71, neutrons= 104, electrons= 71, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 1, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Hf = dict(id= 72, symbol= 'Hf', name= 'Hafnium', atomic_number= 72, mass= '178.49', period= 6, row= 6, column= 4, _group= '4B', protons= 72, neutrons= 106, electrons= 72, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 2, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ta = dict(id= 73, symbol= 'Ta', name= 'Tantalum', atomic_number= 73, mass= '180.94788', period= 6, row= 6, column= 5, _group= '5B', protons= 73, neutrons= 108, electrons= 73, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 3, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
W = dict(id= 74, symbol= 'W', name= 'Tungsten', atomic_number= 74, mass= '183.84', period= 6, row= 6, column= 6, _group= '6B', protons= 74, neutrons= 110, electrons= 74, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 4, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Re = dict(id= 75, symbol= 'Re', name= 'Rhenium', atomic_number= 75, mass= '186.207', period= 6, row= 6, column= 7, _group= '7B', protons= 75, neutrons= 111, electrons= 75, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 5, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Os = dict(id= 76, symbol= 'Os', name= 'Osmium', atomic_number= 76, mass= '190.23', period= 6, row= 6, column= 8, _group= '8B', protons= 76, neutrons= 114, electrons= 76, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 6, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ir = dict(id= 77, symbol= 'Ir', name= 'Iridium', atomic_number= 77, mass= '192.217', period= 6, row= 6, column= 8, _group= '8B', protons= 77, neutrons= 114, electrons= 77, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 7, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Pt = dict(id= 78, symbol= 'Pt', name= 'Platinum', atomic_number= 78, mass= '195.084.', period= 6, row= 6, column= 10, _group= '8B', protons= 78, neutrons= 117, electrons= 78, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 1, _4f1 = 14, _5d= 9, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Au = dict(id= 79, symbol= 'Au', name= 'Gold', atomic_number= 79, mass= '196.966569', period= 6, row= 6, column= 11, _group= '1B', protons= 79, neutrons= 118, electrons= 79, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 1, _4f1 = 14, _5d= 10, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Hg = dict(id= 80, symbol= 'Hg', name= 'Mercury', atomic_number= 80, mass= '200.592', period= 6, row= 6, column= 12, _group= '2B', protons= 80, neutrons= 121, electrons= 80, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Tl = dict(id= 81, symbol= 'Tl', name= 'Thallium', atomic_number= 81, mass= '200.592', period= 6, row= 6, column= 12, _group= '2B', protons= 81, neutrons= 123, electrons= 81, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 1, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Pb = dict(id= 82, symbol= 'Ti', name= 'Lead', atomic_number= 82, mass= '200.592', period= 6, row= 6, column= 12, _group= '2B', protons= 82, neutrons= 125, electrons= 82, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 2, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Bi = dict(id= 83, symbol= 'Bi', name= 'Bismuth', atomic_number= 83, mass= '208.98040', period= 6, row= 6, column= 12, _group= '2B', protons= 83, neutrons= 126, electrons= 83, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 3, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Po = dict(id= 84, symbol= 'Po', name= 'Polonium', atomic_number= 84, mass= '209', period= 6, row= 6, column= 12, _group= '2B', protons= 84, neutrons= 125, electrons= 84, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 4, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
At = dict(id= 85, symbol= 'At', name= 'Astatine', atomic_number= 85, mass= '210', period= 6, row= 6, column= 12, _group= '2B', protons= 85, neutrons= 125, electrons= 85, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 5, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Rn = dict(id= 86, symbol= 'Rn', name= 'Radon', atomic_number= 86, mass= '222', period= 6, row= 6, column= 12, _group= '2B', protons= 86, neutrons= 136, electrons= 86, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Fr = dict(id= 87, symbol= 'Fr', name= 'Francium', atomic_number= 87, mass= '223', period= 7, row= 7, column= 1, _group= '1A', protons= 87, neutrons= 136, electrons= 87, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 1, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ra = dict(id= 88, symbol= 'Ra', name= 'Radium', atomic_number= 88, mass= '226', period= 7, row= 7, column= 2, _group= '2A', protons= 88, neutrons= 138, electrons= 88, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 2, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ac = dict(id= 89, symbol= 'Ac', name= 'Actinium', atomic_number= 89, mass= '227', period= 7, row= 7, column= 4, _group= '20', protons= 89, neutrons= 139, electrons= 89, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Th = dict(id= 90, symbol= 'Th', name= 'Thorium', atomic_number= 90, mass= '232.0377', period= 7, row= 7, column= 5, _group= '20', protons= 90, neutrons= 142, electrons= 90, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Pa = dict(id= 91, symbol= 'Pa', name= 'Protactinium', atomic_number= 91, mass= '231.03588', period= 7, row= 7, column= 6, _group= '20', protons= 91, neutrons= 140, electrons= 91, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
U = dict(id= 92, symbol= 'U', name= 'Uranium', atomic_number= 92, mass= '238.0289', period= 7, row= 7, column= 7, _group= '20', protons= 92, neutrons= 146, electrons= 92, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Np = dict(id= 93, symbol= 'Np', name= 'Neptunium', atomic_number= 93, mass= '237', period= 7, row= 7, column= 8, _group= '20', protons= 93, neutrons= 144, electrons= 93, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Pu = dict(id= 94, symbol= 'Pa', name= 'Plutonium', atomic_number= 91, mass= '244', period= 7, row= 7, column= 9, _group= '20', protons= 94, neutrons= 145, electrons= 94, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Am = dict(id= 95, symbol= 'Am', name= 'Americium', atomic_number= 91, mass= '243', period= 7, row= 7, column= 10, _group= '20', protons= 95, neutrons= 148, electrons= 95, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Cm = dict(id= 96, symbol= 'Cm', name= 'Curium', atomic_number= 91, mass= '247', period= 7, row= 7, column= 11, _group= '20', protons= 96, neutrons= 151, electrons= 96, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Bk = dict(id= 97, symbol= 'Bk', name= 'Berkelium', atomic_number= 97, mass= '247', period= 7, row= 7, column= 12, _group= '20', protons= 97, neutrons= 150, electrons= 97, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Cf = dict(id= 98, symbol= 'Cf', name= 'Californium', atomic_number= 98, mass= '251', period= 7, row= 7, column= 13, _group= '20', protons= 98, neutrons= 153, electrons= 98, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Es = dict(id= 99, symbol= 'Es', name= 'Einsteinium', atomic_number= 99, mass= '252', period= 7, row= 7, column= 14, _group= '20', protons= 99, neutrons= 153, electrons= 99, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Fm = dict(id= 100, symbol= 'Fm', name= 'Fermium', atomic_number= 101, mass= '257', period= 7, row= 7, column= 15, _group= '20', protons= 100, neutrons= 157, electrons= 100, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Md = dict(id= 101, symbol= 'Md', name= 'Mendelevium', atomic_number= 101, mass= '258', period= 7, row= 7, column= 16, _group= '20', protons= 101, neutrons= 157, electrons= 101, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
No = dict(id= 102, symbol= 'No', name= 'Nobelium', atomic_number= 102, mass= '259', period= 7, row= 7, column= 17, _group= '20', protons= 102, neutrons= 157, electrons= 102, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Lr = dict(id= 103, symbol= 'Lr', name= 'Lawrencium', atomic_number= 103, mass= '262', period= 7, row= 7, column= 18, _group= '20', protons= 103, neutrons= 159, electrons= 103, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Rf = dict(id= 104, symbol= 'Rf', name= 'Ruthorfordium', atomic_number= 104, mass= '267', period= 7, row= 7, column= 4, _group= '21', protons= 104, neutrons= 159, electrons= 104, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Db = dict(id= 105, symbol= 'Db', name= 'Dudmium', atomic_number= 105, mass= '268', period= 7, row= 7, column= 5, _group= '21', protons= 105, neutrons= 159, electrons= 105, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Sg = dict(id= 106, symbol= 'Sg', name= 'Seaborgium', atomic_number= 106, mass= '271', period= 7, row= 7, column= 6, _group= '21', protons= 106, neutrons= 159, electrons= 106, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Bh = dict(id= 107, symbol= 'Bh', name= 'Bohrium', atomic_number= 107, mass= '272', period= 7, row= 7, column= 7, _group= '21', protons= 107, neutrons= 159, electrons= 107, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Hs = dict(id= 108, symbol= 'Hs', name= 'Hassium', atomic_number= 108, mass= '270', period= 7, row= 7, column= 8, _group= '21', protons= 108, neutrons= 159, electrons= 108, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Mt = dict(id= 109, symbol= 'Mt', name= 'Meitnerium', atomic_number= 109, mass= '276', period= 7, row= 7, column= 9, _group= '21', protons= 109, neutrons= 159, electrons= 109, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ds = dict(id= 110, symbol= 'Ds', name= 'Darmstadtium', atomic_number= 110, mass= '281', period= 7, row= 7, column= 10, _group= '21', protons= 110, neutrons= 159, electrons= 110, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Rg = dict(id= 111, symbol= 'Rg', name= 'Roentgenium', atomic_number= 111, mass= '280', period= 7, row= 7, column= 11, _group= '21', protons= 111, neutrons= 159, electrons= 111, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Cn = dict(id= 112, symbol= 'Cn', name= 'Copernicium', atomic_number= 112, mass= '285', period= 7, row= 7, column= 13, _group= '21', protons= 112, neutrons= 159, electrons= 112, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Nh = dict(id= 113, symbol= 'Nh', name= 'Nihonium', atomic_number= 113, mass= '284', period= 7, row= 7, column= 13, _group= '21', protons= 113, neutrons= 159, electrons= 113, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Fl = dict(id= 114, symbol= 'Fl', name= 'Flerovium', atomic_number= 114, mass= '289', period= 7, row= 7, column= 14, _group= '21', protons= 114, neutrons= 159, electrons= 114, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Mc = dict(id= 115, symbol= 'Mc', name= 'Moscovium', atomic_number= 115, mass= '288', period= 7, row= 7, column= 15, _group= '21', protons= 115, neutrons= 159, electrons= 115, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Lv = dict(id= 116, symbol= 'Lv', name= 'Livermorium', atomic_number= 116, mass= '293', period= 7, row= 7, column= 16, _group= '21', protons= 116, neutrons= 159, electrons= 116, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ts = dict(id= 117, symbol= 'Ts', name= 'Tennessine', atomic_number= 117, mass= '294', period= 7, row= 7, column= 17, _group= '21', protons= 117, neutrons= 159, electrons= 117, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Og = dict(id= 118, symbol= 'Og', name= 'Oganesson', atomic_number= 118, mass= '294', period= 7, row= 7, column= 18, _group= '21', protons= 118, neutrons= 159, electrons= 118, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')

db = {}
db['H'] = H
db['He'] = He
db['Li'] = Li
db['Be'] = Be
db['B'] = B
db['C'] = C
db['N'] = N
db['O'] = O
db['F'] = F
db['Ne'] = Ne
db['Na'] = Na
db['Mg'] = Mg
db['Al'] = Al
db['Si'] = Si
db['P'] = P
db['S'] = S
db['Cl'] = Cl
db['Ar'] = Ar
db['K'] = K
db['Ca'] = Ca
db['Sc'] = Sc
db['Ti'] = Ti
db['V'] = V
db['Cr'] = Cr
db['Mn'] = Mn
db['Fe'] = Fe
db['Co'] = Co
db['Ni'] = Ni
db['Cu'] = Cu
db['Zn'] = Zn
db['Ga'] = Ga
db['Ge'] = Ge
db['As'] = As
db['Se'] = Se
db['Br'] = Br
db['Kr'] = Kr
db['Rb'] = Rb
db['Sr'] = Sr
db['Y'] = Y
db['Zr'] = Zr
db['Nb'] = Nb
db['Mo'] = Mo
db['Tc'] = Tc
db['Ru'] = Ru
db['Rh'] = Rh
db['Pd'] = Pd
db['Ag'] = Ag
db['Cd'] = Cd
db['La'] = La
db['Ce'] = Ce
db['Pr'] = Pr
db['Nd'] = Nd
db['Pm'] = Pm
db['Sm'] = Sm
db['Eu'] = Eu
db['Gd'] = Gd
db['Tb'] = Tb
db['Dy'] = Dy
db['Ho'] = Ho
db['Er'] = Er
db['Tm'] = Tm
db['Yb'] = Yb
db['Lu'] = Lu
db['Hf'] = Hf
db['Ta'] = Ta
db['W'] = W
db['Re'] = Re
db['Os'] = Os
db['Ir'] = Ir
db['Pt'] = Pt
db['Au'] = Au
db['Hg'] = Hg
db['Tl'] = Tl
db['Pb'] = Pb
db['Bi'] = Bi
db['Po'] = Po
db['At'] = At
db['Rn'] = Rn
db['Fr'] = Fr
db['Ra'] = Ra
db['Ac'] = Ac
db['Th'] = Th
db['Pa'] = Pa
db['U'] = U
db['Np'] = Np
db['Pu'] = Pu
db['Am'] = Am
db['Cm'] = Cm
db['Bk'] = Bk
db['Cf'] = Cf
db['Es'] = Es
db['Fm'] = Fm
db['Md'] = Md
db['No'] = No
db['Lr'] = Lr
db['Rf'] = Rf
db['Db'] = Db
db['Sg'] = Sg
db['Bh'] = Bh
db['Hs'] = Hs
db['Mt'] = Mt
db['Ds'] = Ds
db['Rg'] = Rg
db['Cn'] = Cn
db['Nh'] = Nh
db['Fl'] = Fl
db['Mc'] = Mc
db['Lv'] = Lv
db['Ts'] = Ts
db['Og'] = Og

#create_element_dict()
elements_symbols_list = "Ac Ag Al Am Ar As At Au B Ba Be Bi Bk Br C Ca Cd Ce Cf Cl Cm Co Cr Cs Cu Dy Er Es Eu " \
                        "F Fe Fm Fr Ga Gd Ge H He Hf Hg Ho I In Ir K Kr La Li Lu Md Mn Mo N Na Nb Nd Ne Ni Np O Os " \
                        "P Pa Pb Pd Pm Po Pr Pt Pu Ra Rb Re Rh Rn  Ru S Sb Sc Se Si Sm Sn Sr Ta Tb Tc Te Th Ti Tl Tm" \
                        "U V W Xe Y Yb Zn Zr "
''' An element name list is used to fill the element name combo box to help the user who knows
the name of an element, but not the symbols. '''
elements_name_list = "Actinium Silver Aluminum Americium Argon Arsenic Astatine Gold Boron Barium Beryllium " \
                     "Bismuth Berkelium Bromine Carbon Calcium Cadmium Cerium Californium Chlorine Curium Cobalt Chromium " \
                     "Cesium Copper Dysprosium Erbium Einsteinium Europium Fluorine Iron Fermium Francium Gallium Gadolinium " \
                     "Germanium Hydrogen Helium Hafnium Mercury Holmium Iodine Indium Iridium Potassium Krypton " \
                     "Lanthanum Lithium Lutetium Mendelevium Manganese Molybdenum Nitrogen Na Niobium Neodymium Neon Nickel " \
                     "Neptunium Oxygen Osmium Phosphorus Protactinium Lead Palladium Promethium Polonium Praseodymium " \
                     "Platnum Plutonium Radium Rubidium Rhenium Rhodium Radon Rutherfordium Sulfur Antimony Scandium Selenium Silicon " \
                     "Samarium Tin Strontium Tantalum Terbium Technetium Tellurium Thorium Titanium " \
                     "Thallium Thulium Uranium Vanadium Tungsten Xenon Yttrium Ytterbium Zinc Zirconium "


compound_name_string = "aluminum_carbide aluminum_chloride air boron_trichloride methane ethane propane butane 2-methylpropane" \
                      " pentane hexane heptane octane nonane decane tetradecane octadecane calcium_dihydrogen_phosphate" \
                      " calcium_iodide calcium_hydroxide calcium_phosphide cadmium_sulfide cesium_fluoride citric_acid" \
                      " acetic_acid acetic_acid carbon_monoxide carbon_dioxide hydrogen_bromide " \
                      " acetic_acid hydrogen_chloride hydrochloric_acid perchloric_acid hydrogen_cyanide" \
                      " carbonic_acid hydrogen_fluoride hydrofluoric_acid hydrogen_iodide nitrous_acid" \
                      " nitric_acid phosphoric_acid hydrogen_suflide sulfurous_acid sulfuric_acid" \
                      " iodine_heptafluoride potassium_bromide potassium_hydroxide lithium_chloride magnesium_nitride" \
                      " sodium_chloride bicarbonate_of_soda sodium_oxide sodium_hydroxide sodium_sulfate ammonia hydrazine nitric_oxide" \
                      " nitorgen_dioxide dinitrogen_tetroxide nitrous_oxide dinitrogen_pentoxide phosphorus_pentafluoride" \
                      " sulfur_dioxide sulfur_trioxide"
''' This list of compounds and names will help retrieve names from formulas. Doesn't work. Why? '''
compound_names_dict = {'aluminum_carbide': 'Al4C3', 'aluminum_chloride': 'AlCl3', 'air': 'Ar2He2Kr2Ne2Xe2Rn2',
                        'boron_trichloride': 'BCl3', 'methane': 'CH4', 'ethane': 'C2H6', 'propane': 'C3H8',
                        'butane': 'C4H10', '2-methylpropane': 'C4H10_M', 'pentane': 'C5H12', 'hexane': 'C6H14',
                        'heptane': 'C7H16', 'octane': 'C8H18', 'nonane': 'C9H20', 'decane': 'C10H22',
                        'tetradecane': 'C14H30', 'octadecane': 'C18H38', 'calcium_dihydrogen_phosphate': 'CaH2PO4',
                        'calcium_iodide': 'CaI', 'calcium_hydroxide': 'CaOH2', 'calcium_phosphide': 'Ca3P2',
                        'cadmium_sulfide': 'CdS', 'cesium_fluoride': 'CsF', 'citric_acid': 'C6H8O7',
                        'acetic_acid': 'HC2H3O2', 'carbon_monoxide': 'CO', 'carbon_dioxide': 'CO2',
                        'hydrogen_bromide': 'HBr',
                        'hydrochloric_acid': 'HCl', 'perchloric_acid': 'HClO4', 'hydrogen_cyanide': 'HCN',
                        'carbonic_acid': 'H2CO3', 'hydrofluoric_acid': 'HF',
                        'hydroiodic_acid': 'HI', 'nitrous_acid': 'HNO2',
                        'nitric_acid': 'HNO3', 'phosphoric_acid': 'H3PO4',
                        'hydrosulfuric_acid': 'H2S', 'sulfurous_acid': 'H2SO3', 'sulfuric_acid': 'H2SO4',
                        'iodine_heptafluoride': 'IF7', 'potassium_bromide': 'KBr', 'potassium_hydroxide': 'KOH',
                        'lithium_chloride': 'LiCl', 'magnesium_nitride': 'Mg3N2', 'sodium_chloride': 'NaCl',
                        'bicarbonate_of_soda': 'NaHCO3', 'sodium_oxide': 'Na2O', 'sodium_hydroxide': 'NaOH',
                        'sodium_sulfate': 'Na2SO4', 'ammonia': 'NH3', 'hydrazine': 'N2H4', 'nitric_oxide': 'NO',
                        'nitorgen_dioxide': 'NO2', 'dinitrogen_tetroxide': 'N2O4', 'nitrous_oxide': 'N2O',
                        'dinitrogen_pentoxide': 'N2O5', 'phosphorus_pentafluoride': 'PF5', 'sulfur_dioxide': 'SO2',
                        'sulfur_trioxide': 'SO3'}
ion_names_dict = {'acetate': 'C2H3O2', 'chlorite': 'ClO2', 'chlorate': 'ClO3', 'perchlorate': 'ClO4',
                  'cyanide': 'CN', 'carbonate': 'CO32', 'copper_(II)_sulfide': 'CuS', 'iron_(II)_chloride': 'FeCl2',
                  'iron_(III)_chloride': 'FeCl3', 'dihydrogen_phosphate': 'H2PO4', 'hydrogen_carbonate': 'HCO3',
                  'mercury_(I)_oxide': 'Hg2O', 'mercury_(II)_oxide': 'HgO', 'hydronium': 'H3O',
                  'hydrogen_phosphate': 'HPO42', 'hydrogen_sulfate': 'HSO4', 'hydroxide': 'OH',
                  'ammonium': 'NH4', 'nitrate': 'NO3', 'nitrite': 'NO2',
                  'permanganate': 'MnO4', 'peroxide': 'H2O22', 'sulfate': 'SO42',
                  'sulfite': 'SO32', 'phosphate': 'PO43'}
ion_symbols_list = "C2H3O2 ClO2 ClO3 ClO4 CN CO32 CuS FeCl2 FeCl3 H2PO4 HCO3 Hg2O HgO H3O HPO42 HSO4 OH NH4 NO3 NO2 MnO4 O22 SO42 SO32 PO43"
ion_names_list = "acetate chlorite chlorate perchlorate cyanide carbonate copper_(II)_sulfide " \
                 "iron_(II)_chloride iron_(III)_chloride dihydrogen_phosphate hydrogen_carbonate " \
                 "mercury_(I)_oxide mercury_(II)_oxide hydronium hydrogen_phosphate hydrogen_sulfate " \
                 "hydroxide ammonium nitrate nitrite permanganate peroxide sulfate sulfite phosphate "
eci_1_d = dict(eci = 'eci_1', eci_type = "", name ="", column = "", electronegativity = "", _group = "",
                 display_qty = "", qty = "", M_qty = "" , mass = "", Oxidation_State ="", display_units = "", units = "", valence = "",
                 display_temp_units= "", display_temp_qty="", display_press_units= "", display_press_qty= "",
                 temp_units= "", temp_qty="", press_units= "", press_qty= "")
acids_symbol_string = "No list yet"
acids_names_string = "No list yet"
bases_symbol_string = "No list yet"
bases_symbol_string = "No list yet"
bases_names_string = "No list yet"

unit_values = "Moles grams kilograms ounces pounds liters(l) liters(g) ml(l) ml(g)"
environment = "Laboratory Industry Nature"
temp_units = "K F C"
press_units = "atm torr psi mmHg"
equipment = "refinery blah1 blah2"
energy_type = "heat electricity"
catalyst = "blah1 blah2 blah3 blah4"
side_effects = "air_polution water_polution land_polution"
by_products = "CO CO2 NO NO2"
variables = "Av Bv Cv Kv"  # Variable names cannot conflict with element symbols like B C H K etc

def define_variables():
    pass
record_name = ""  # This is a placeholder for a record name to store the process in the database.
''' The following are lists of variables to fill various combo boxes until proper lists are made. '''

''' Variables to hold the selected items of combo boxes. '''
#process_selected = ""
equipment_selected = ""
energy_type_selected = ""
catalyst_selected = ""
side_effect_selected = ""
by_product_selected = ""
variable_selected = ""
variable_value = DoubleVar()
Init_default_T_and_P = FALSE
Av = DoubleVar()
Bv = DoubleVar()
Cv = DoubleVar()
Kv = DoubleVar()
''' Miscellaneous variables to use until proper variables are created. '''
valences = "7 6 5 4 3 2 1 0 -1 -2 -3 -4"
default_temp_units = StringVar()
default_temp_qty = DoubleVar()
default_press_units = StringVar()
default_press_qty = DoubleVar()
eci_1 = StringVar()
eci_2 = StringVar()
eci_3 = StringVar()
eci_4 = StringVar()
eci_5 = StringVar()
eci_6 = StringVar()
eci_1_col = IntVar()
eci_2_col = IntVar()
eci_3_col = IntVar()
eci_4_col = IntVar()
eci_5_col = IntVar()
eci_6_col = IntVar()
eci_1_electronegativity = DoubleVar()
eci_2_electronegativity = DoubleVar()
eci_3_electronegativity = DoubleVar()
eci_4_electronegativity = DoubleVar()
eci_5_electronegativity = DoubleVar()
eci_6_electronegativity = DoubleVar()
eci_1_group = StringVar()
eci_2_group = StringVar()
eci_3_group = StringVar()
eci_4_group = StringVar()
eci_5_group = StringVar()
eci_6_group = StringVar()
eci_1_M_qty = DoubleVar()
eci_2_M_qty = DoubleVar()
eci_3_M_qty = DoubleVar()
eci_4_M_qty = DoubleVar()
eci_5_M_qty = DoubleVar()
eci_6_M_qty = DoubleVar()
eci_1_mass = DoubleVar()
eci_2_mass = DoubleVar()
eci_3_mass = DoubleVar()
eci_4_mass = DoubleVar()
eci_5_mass = DoubleVar()
eci_6_mass = DoubleVar()
eci_1_name = StringVar()
eci_2_name = StringVar()
eci_3_name = StringVar()
eci_4_name = StringVar()
eci_5_name = StringVar()
eci_6_name = StringVar()
eci_1_Oxidation_State = StringVar()
eci_2_Oxidation_State = StringVar()
eci_3_Oxidation_State = StringVar()
eci_4_Oxidation_State = StringVar()
eci_5_Oxidation_State = StringVar()
eci_6_Oxidation_State = StringVar()
eci_1_qty = DoubleVar()
eci_2_qty = DoubleVar()
eci_3_qty = DoubleVar()
eci_4_qty = DoubleVar()
eci_5_qty = DoubleVar()
eci_6_qty = DoubleVar()
eci_1_type = StringVar()
eci_2_type = StringVar()
eci_3_type = StringVar()
eci_4_type = StringVar()
eci_5_type = StringVar()
eci_6_type = StringVar()
eci_1_units = StringVar()
eci_2_units = StringVar()
eci_3_units = StringVar()
eci_4_units = StringVar()
eci_5_units = StringVar()
eci_6_units = StringVar()
eci_1_valence = StringVar()
eci_2_valence = StringVar()
eci_3_valence = StringVar()
eci_4_valence = StringVar()
eci_5_valence = StringVar()
eci_6_valence = StringVar()
eci_1_temp_units = StringVar()
eci_2_temp_units = StringVar()
eci_3_temp_units = StringVar()
eci_4_temp_units = StringVar()
eci_5_temp_units = StringVar()
eci_6_temp_units = StringVar()
eci_temp_1_qty = DoubleVar()
eci_temp_2_qty = DoubleVar()
eci_temp_3_qty = DoubleVar()
eci_temp_4_qty = DoubleVar()
eci_temp_5_qty = DoubleVar()
eci_temp_6_qty = DoubleVar()
eci_1_press_units = StringVar()
eci_2_press_units = StringVar()
eci_3_press_units = StringVar()
eci_4_press_units = StringVar()
eci_5_press_units = StringVar()
eci_6_press_units = StringVar()
eci_press_1_qty = DoubleVar()
eci_press_2_qty = DoubleVar()
eci_press_3_qty = DoubleVar()
eci_press_4_qty = DoubleVar()
eci_press_5_qty = DoubleVar()
eci_press_6_qty = DoubleVar()
energy_amount = DoubleVar()
alpha_4 = StringVar()
molar_mass = DoubleVar()
ion_4_charge = IntVar()
total_mass = DoubleVar()
cb_1_type = ""  # elements compounds ions
cb_2_type = ""
cb_3_type = ""
cb_4_type = ""
cb_5_type = ""
cb_6_type = ""

''' Add functions here'''
def select_eci_1_type(eventObject):
    '''
    Use these comboboxes to load the correct symbols/formulae and names
    in the associated comboboxes
    '''
    print("Entered select_eci_1_type.")
    cb_1_type = cb_Select_CB1.get()  # use cb_1_type as a local variable to improve readability
    #eci_d['eci_1']['eci_type'] = cb_Select_CB1.get()
    dbr['R1']['eci_1_type'] = cb_Select_CB1.get()
    print("dbr['R1']['eci_1_type'] = ", cb_Select_CB1.get())
    # print("cb_1_type is ", cb_1_type)
    ''' Both of the assignments below work. '''
    # print("eci_db['eci_1']['eci_type'] is ", eci_db['eci_1']['eci_type'])
    # print("eci_db['eci_1']['eci_type'] is ", cb_1_type)
    #eci_d['eci_1']['eci_type'] = cb_1_type
    '''
    Use the appropriate symbol and name lists to fill in the comboboxes.
    '''
    if cb_1_type == 'elements':
        cb_eci_1['values'] = element_symbol_string #elements_symbols_list # element_symbol_string
        cb_eci_1_N['values'] = element_name_string #elements_name_list   # element_name_string
    elif cb_1_type == 'compounds':  #ionic-compounds
        cb_eci_1['values'] = compound_formula_string
        cb_eci_1_N['values'] = compound_name_string
    elif cb_1_type == 'ionic_compounds':
        cb_eci_1['values'] = ionic_compounds_symbols_string
        cb_eci_1_N['values'] = ionic_compounds_names_string
    elif cb_1_type == 'ions':
        cb_eci_1['values'] = ion_symbols_list
        cb_eci_1_N['values'] = ion_names_list
    elif cb_1_type == 'acids':
        cb_eci_1['values'] = acids_symbol_string
        cb_eci_1_N['values'] = acids_names_string
    elif cb_1_type == 'bases':
        cb_eci_1['values'] = bases_symbol_string
        cb_eci_1_N['values'] = bases_symbol_string
    elif cb_1_type == 'polyatomic':
        cb_eci_1['values'] = polyatomic_formula_string
        cb_eci_1_N['values'] = polyatomic_name_string
    else:
        print("Error is select_eci_1_type")


def select_eci_2_type(eventObject):
    print("Entered select_eci_2_type.")
    cb_2_type = cb_Select_CB2.get()
    print("cb_2_type is ", cb_2_type)
    dbr['R1']['eci_3_type'] = cb_Select_CB3.get()
    print("dbr['R1']['eci_2_type'] = ", cb_Select_CB2.get())
    eci_d['eci_2']['eci_type'] = cb_Select_CB2.get()
    if cb_2_type == 'elements':
        cb_eci_2['values'] = element_symbol_string
        cb_eci_2_N['values'] = element_name_string
    elif cb_2_type == 'compounds':
        cb_eci_2['values'] = compound_formula_string
        cb_eci_2_N['values'] = compound_name_string
    elif cb_2_type == 'ions':
        cb_eci_2['values'] = ion_symbols_list
        cb_eci_2_N['values'] = ion_names_list
    else:
        print("Error is select_eci_2_type")


def select_eci_3_type(eventObject):
    print("Entered select_eci_3_type.")
    cb_3_type = cb_Select_CB3.get()
    dbr['R1']['eci_3_type'] = cb_Select_CB3.get()
    print("dbr['R1']['eci_3_type'] = ", cb_Select_CB3.get())
    print("cb_3_type is ", cb_3_type)
    eci_d['eci_3']['eci_type'] = cb_Select_CB3.get()
    if cb_3_type == 'elements':
        cb_eci_3['values'] = element_symbol_string
        cb_eci_3_N['values'] = element_name_string
    elif cb_3_type == 'compounds':
        cb_eci_3['values'] = compound_formula_string
        cb_eci_3_N['values'] = compound_name_string
    elif cb_3_type == 'ions':
        cb_eci_3['values'] = ion_symbols_list
        cb_eci_3_N['values'] = ion_names_list
    else:
        print("Error is select_eci_3_type")


def select_eci_4_type(eventObject):
    print("Entered select_eci_4_type.")
    cb_4_type = cb_Select_CB4.get()
    dbr['R1']['eci_4_type'] = cb_Select_CB4.get()
    print("dbr['R1']['eci_4_type'] = ", cb_Select_CB4.get())
    print("cb_4_type is ", cb_4_type)
    eci_d['eci_4']['eci_type'] = cb_Select_CB4.get()
    if cb_4_type == 'elements':
        cb_eci_4['values'] = element_symbol_string
        cb_eci_4_N['values'] = element_name_string
    elif cb_4_type == 'compounds':
        cb_eci_4['values'] = compound_formula_string
        cb_eci_4_N['values'] = compound_name_string
    elif cb_4_type == 'ions':
        cb_eci_4['values'] = ion_symbols_list
        cb_eci_4_N['values'] = ion_names_list
    else:
        print("Error is select_eci_4_type")


def select_eci_5_type(eventObject):
    print("Entered select_eci_5_type.")
    cb_5_type = cb_Select_CB5.get()
    dbr['R1']['eci_5_type'] = cb_Select_CB5.get()
    print("dbr['R1']['eci_5_type'] = ", cb_Select_CB5.get())
    print("cb_5_type is ", cb_5_type)
    eci_d['eci_5']['eci_type'] = cb_Select_CB5.get()
    if cb_5_type == 'elements':
        cb_eci_5['values'] = element_symbol_string
        cb_eci_5_N['values'] = element_name_string
    elif cb_5_type == 'compounds':
        cb_eci_5['values'] = compound_formula_string
        cb_eci_5_N['values'] = compound_name_string
    elif cb_5_type == 'ions':
        cb_eci_5['values'] = ion_symbols_list
        cb_eci_5_N['values'] = ion_names_list
    else:
        print("Error is select_eci_5_type")


def select_eci_6_type(eventObject):
    print("Entered select_eci_6_type.")
    cb_6_type = cb_Select_CB6.get()
    dbr['R1']['eci_6_type'] = cb_Select_CB6.get()
    print("dbr['R1']['eci_6_type'] = ", cb_Select_CB6.get())
    print("cb_6_type is ", cb_6_type)
    eci_d['eci_6']['eci_type'] = cb_Select_CB6.get()
    if cb_6_type == 'elements':
        cb_eci_6['values'] = element_symbol_string
        cb_eci_6_N['values'] = element_name_string
    elif cb_6_type == 'compounds':
        cb_eci_6['values'] = compound_formula_string
        cb_eci_6_N['values'] = compound_name_string
    elif cb_6_type == 'ions':
        cb_eci_6['values'] = ion_symbols_list
        cb_eci_6_N['values'] = ion_names_list
    else:
        print("Error is select_eci_6_type")


''' Start defining process and chemistry related functions '''


def create_record():
    ''' print("Pressed create_record button") '''


def get_record():
    ''' print("Pressed get_record button") '''


def retrieve_record():
    ''' print("Pressed retrieve_record button") '''


def previous_record():
    ''' print("Pressed previous_record button") '''


def next_record():
    ''' print("Pressed next_record button") '''


def update_record():
    ''' print("Pressed update_record button") '''

def print_R1():
    """ Print the record of the first eci to verify record."""
    print("dbr['R1']['eci_1_type'] is ", dbr['R1']['eci_1_type'])
    print("dbr['R1']['eci_1_formula'] is ", dbr['R1']['eci_1_formula'])
    print("dbr['R1']['eci_1_name'] is ", dbr['R1']['eci_1_name'])
    print("dbr['R1']['eci_1_units'] is ", dbr['R1']['eci_1_units'])
    print("dbr['R1']['eci_1_qty'] is ", dbr['R1']['eci_1_qty'])
    print("dbr['R1']['eci_1_M_qty'] is ", dbr['R1']['eci_1_M_qty'])
    print("dbr['R1']['eci_1_temp_display_units'] is ", dbr['R1']['eci_1_temp_display_units'])
    print("dbr['R1']['eci_1_temp_calc_units'] is ", dbr['R1']['eci_1_temp_calc_units'])
    print("dbr['R1']['eci_1_temp_display_qty'] is ", dbr['R1']['eci_1_temp_display_qty'])
    print("dbr['R1']['eci_1_temp_calc_qty'] is ", dbr['R1']['eci_1_temp_calc_qty'])
    print("dbr['R1']['eci_1_press_display_units'] is ", dbr['R1']['eci_1_press_display_units'])
    print("dbr['R1']['eci_1_press_calc_units'] is ", dbr['R1']['eci_1_press_calc_units'])
    print("dbr['R1']['eci_1_press_display_qty'] is ", dbr['R1']['eci_1_press_display_qty'])
    print("dbr['R1']['eci_1_press_calc_qty'] is ", dbr['R1']['eci_1_press_calc_qty'])
    print("end of dbr['R1']['eci_1_formula'] print function.")

def minor_process_selected(eventObject):
    """ print("process_selected") """
    # if process_selected == Calculate:
    # Change the following message to a window with instructions.
    #showinfo(title=None, message="To calculate eci variables, enter an element type and symbol and a mole quantity.")
    #tkMessageBox.showinfo(message='Hello')
    #"Set_STP_Variables Pressure Volume, moles Temperature pvnrt"
    print('1068 minor_process_selected function entered.', eventObject)
    if minor_process_selected == Set_STP_Variables():
        print("In Continue function at major_process_selected == 'Set_STP_Variables'")
        ''' Continue the Set_STP_Variables process '''
    elif minor_process_selected == 'pvnrt':
        pvnrt()
    else: print('minor_process_selected fell thru to else clause.')

def Set_STP_Variables():
    print('1075 Set_STP_Variables function entered.')
    eci_1_temp_units = cb_1_Temp_Units.set('C')
    e_Temp_Qty_1.delete(0, tk.END)
    e_Temp_Qty_1.insert(0, 0)
    eci_1_press_units = cb_1_Press_Units.set('atm')
    e_Press_Qty_1.delete(0, tk.END)
    e_Press_Qty_1.insert(0, 1.0)
    """
    Set the initial units and values of temperature and pressure to standard temperature and pressure
    (0°C) and  (1 atm)
    """
    ''' The following code works to set initial STP variables for all 6 frames. '''
    eci_1_temp_units = cb_1_Temp_Units.set('C')
    e_Temp_Qty_1.delete(0, tk.END)
    e_Temp_Qty_1.insert(0, 0)
    dbr['R1']['eci_1_temp_display_qty'] = e_Temp_Qty_1
    eci_1_press_units = cb_1_Press_Units.set('atm')
    e_Press_Qty_1.delete(0, tk.END)
    e_Press_Qty_1.insert(0, 1.0)
    dbr['R1']['eci_1_press_display_qty'] = e_Press_Qty_1
    eci_2_temp_units = cb_2_Temp_Units.set('C')
    e_Temp_Qty_2.delete(0, tk.END)
    e_Temp_Qty_2.insert(0, 0)
    eci_2_press_units = cb_2_Press_Units.set('atm')
    e_Press_Qty_2.delete(0, tk.END)
    e_Press_Qty_2.insert(0, 1.0)
    eci_3_temp_units = cb_3_Temp_Units.set('C')
    e_Temp_Qty_3.delete(0, tk.END)
    e_Temp_Qty_3.insert(0, 0)
    eci_1_press_units = cb_3_Press_Units.set('atm')
    e_Press_Qty_3.delete(0, tk.END)
    e_Press_Qty_3.insert(0, 1.0)
    eci_4_temp_units = cb_4_Temp_Units.set('C')
    e_Temp_Qty_4.delete(0, tk.END)
    e_Temp_Qty_4.insert(0, 0)
    eci_4_press_units = cb_4_Press_Units.set('atm')
    e_Press_Qty_4.delete(0, tk.END)
    e_Press_Qty_4.insert(0, 1.0)
    eci_5_temp_units = cb_5_Temp_Units.set('C')
    e_Temp_Qty_5.delete(0, tk.END)
    e_Temp_Qty_5.insert(0, 0)
    eci_5_press_units = cb_5_Press_Units.set('atm')
    e_Press_Qty_5.delete(0, tk.END)
    e_Press_Qty_5.insert(0, 1.0)
    eci_6_temp_units = cb_6_Temp_Units.set('C')
    e_Temp_Qty_6.delete(0, tk.END)
    e_Temp_Qty_6.insert(0, 0)
    eci_6_press_units = cb_6_Press_Units.set('atm')
    e_Press_Qty_6.delete(0, tk.END)
    e_Press_Qty_6.insert(0, 1.0)
    print_R1()


def check_entry_changes():
    print('1126 check_entry_changes function entered.')
    '''
    When an entry is made, check the value and assign it to an r dictionary field.
    '''
    '''eci_1_d = dict(eci = 'eci_1', eci_type = "", name ="", column = "", electronegativity = "", _group = "",
                 display_qty = "", qty = "", M_qty = "" , mass = "", Oxidation_State ="", display_units = "", units = "", valence = "",
                 display_temp_units= "", display_temp_qty="", display_press_units= "", display_press_qty= "",
                 temp_units= "", temp_qty="", press_units= "", press_qty= "")
    '''
    #print("In check_entry_changes")
    ''' The following don't seem necessary. '''
    #eci_1_type = cb_Select_CB1.get()
    #eci_1 = cb_eci_1.get()
    #eci_1_qty = e_eci_1_qty.get()
    #eci_1_units = cb_eci_1_units.get()
    #dbr['R1']['eci_1_formula'] = cb_eci_1.get()
    #r1['eci_1_formula']['eci'] = eci_1
    #r1['eci_1']['eci'] = eci_1
    #r1['eci_1_type']['type'] = eci_1_type
    #if eci_1_units == "":
    #   cb_eci_1_units.set('grams')
    #    r1['eci_1']['display_units'] = cb_eci_1_units.get()
    #    r1['eci_1']['display_temp_units'] = cb_1_Temp_Units.get()
    #    r1['eci_1']['display_temp_qty'] = e_Temp_Qty_1.get()
    #    r1['eci_1']['display_press_units'] = cb_1_Press_Units.get()
    #    r1['eci_1']['display_press_qty'] = e_Press_Qty_1.get()
    #if eci_1_type == 'elements':
    #    eci_1_mass = getdouble(db[eci_1]['mass'])   # Get element mass from the dictionary of element dictionaries
    #    r1['eci_1']['mass'] = getdouble(db[eci_1]['mass'])   #set the eci_frame mass field to the element mass
    #    ''' Need to move the following to a separate function because qty may be input or calculated
    #        or qualify it as an imput or a calculated value. Won't it normally be a calculated value? '''
    #    r1['eci_1']['display_qty'] = e_eci_1_qty.get()

    #    #eci_1_M_qty = getdouble(db[eci_1]['mass'])  # don't use float due to precision errors
    #    eci_1_M_qty = getdouble(e_eci_1_M_qty.get())
    #    m_mass = eci_1_M_qty * getdouble(db[eci_1]['mass'])
    #    e_eci_1_qty.insert(0, m_mass)   #eci_1_mass)
    #    print("m_mass is ", m_mass)
    #    print("m_mass is ",  getdouble(eci_1_M_qty) * getdouble(db[eci_1]['mass'])) #getdouble(e_eci_1_M_qty.get()) eci_1_M_qty


    #elif eci_1_type == 'compounds':
    #    pass
    #    ''' Compounds and ions don't currently have a mass property '''
    #    #eci_1_mass = getdouble(c_db[eci_1]['mass'])
    #    #e_eci_1_qty.insert(0, eci_1_mass)
    #elif eci_1_type == 'ions':
    #    pass
    #    ''' Compounds and ions don't currently have a mass property '''
        #eci_1_mass = getdouble(i_db[eci_1]['mass'])
        #e_eci_1_qty.insert(0, eci_1_mass)

    #print("e_eci_1_qty.get() is ", e_eci_1_qty.get())
    #print("eci_db['eci_1']['qty'] is ", eci_d['eci_1']['qty'])
    #print("e_eci_1_M_qty.get() is ", e_eci_1_M_qty.get())
    #print("eci_1_qty is ", e_eci_1_qty.get())  # eci_1_qty is  PY_VAR54
    #print("eci_db['eci_1']['qty'] is ", eci_1_qty)


    #The following works.
    '''
    total_mass = getdouble(e_eci_1_qty.get()) * eci_1_mass  # float(db[eci_1]['mass'])
    print("total_mass is ", total_mass)
    eci_d['eci_1']['qty'] = total_mass
    print("eci_db['eci_1']['qty'] ", eci_d['eci_1']['qty'])
    '''
def major_process_selected():
    print("1193 In Continue function at major_process_selected")
    Continue()

def Continue():
    ''' A button/function to continue whatever process was selected. '''
    print("1198 In Continue function")
    major_process_selected = cb_Select_M_Process.get() #cb_Select_Process.get()
    minor_process_selected = cb_Select_m_Process.get()
    #print("Process selected is ", process_selected)
    # check_entry_changes(
    #
    if major_process_selected == 'Acid_Base':
        print("In Continue function at major_process_selected == 'Acid_Base'")
        ''' Continue the Acid_Base process '''
        Acid_Base()
    elif major_process_selected == 'Balance_Equation':
        print("In Continue function at major_process_selected == 'Balance_Equation'")
        Balance_Equation()
    elif major_process_selected == 'Calculate':
        print("In Continue function at major_process_selected == 'Calculate'")

        ''' Continue the Calculate process '''
        check_entry_changes()
        #calculate()
    elif major_process_selected == 'Decompose':
        print("In Continue function at major_process_selected == 'Decompose'")
        """ Continue the Decompose process """
        Decompose()
    elif major_process_selected == 'Set_default_T_and_P':
        print("In Continue function at major_process_selected == 'Set_default_T_and_P'")
        """ Continue the Initialize_default_T_and_P process """
        #if Init_default_T_and_P == FALSE:
        #    pdb.set_trace()
        #    Initialize_default_T_and_P()
        #    Init_default_T_and_P == TRUE
        set_t_and_p_inst = "Set the default temperature and pressure settings you want to use" \
                           "for the current process. Select Set_default_T_and_P from the Process " \
                           "combobox, then select/set the temperature and pressure units and quantities" \
                           "in the first eci frame. Then press the Continue button. After you have set these" \
                           "defaults, select the next process. "
        e_Explanation.insert(END, set_t_and_p_inst)
        Set_default_T_and_P()
    elif major_process_selected == 'Oxidation_Reduction':
        print("In Continue function at major_process_selected == 'Oxidation_Reduction'")
        """ Continue the Oxidation_Reduction process """
        Oxidation_Reduction()
    elif major_process_selected == 'Metathesis':
        print("In Continue function at major_process_selected == 'Metathesis'")
        """ Continue the Metathesis process """
        Metathesis()
    elif major_process_selected == 'Oxidation_Rate':
        print("In Continue function at major_process_selected == 'Oxidation_Rate'")
        """ Continue the Oxidation_Rate process """
        Oxidation_Rate()
    elif major_process_selected == 'Parse_Reactants':
        print("In Continue function at major_process_selected == 'Parse_Reactants'")
        ''' There is a general procedure used to prove parse works,
        and a procedure tied to the eci_1 combobox. '''
        Parse_Reactants()
    elif major_process_selected == 'Parse_Products':
        print("In Continue function at major_process_selected == 'Parse_Products'")
        ''' There is a general procedure used to prove parse works,
        and a procedure tied to the eci_1 combobox. '''
        Parse_Products()
    elif major_process_selected == 'Precipitation':
        print("In Continue function at major_process_selected == 'Precipitation'")
        """ Continue the Precipitation process """
        Precipitation()
    elif major_process_selected == 'Reduction':
        print("In Continue function at major_process_selected == 'Reduction'")
        """ Continue the Reduction process """
        Reduction()
    elif major_process_selected == 'Refine':
        print("In Continue function at major_process_selected == 'Refine'")
        """ Continue the Refine process """
        Refine()
    elif major_process_selected == 'Synthesis':
        print("In Continue function at major_process_selected == 'Synthesis'")
        """ Continue the Synthesis process """
        Synthesis()

    elif minor_process_selected == "Set_STP_Variables":
        print("In Continue function at major_process_selected == 'Set_STP_Variables'")
        Set_STP_Variables()
    elif minor_process_selected == 'pvnrt':
        pvnrt()
    elif minor_process_selected == 'vol_from_prt':
        vol_from_prt()
    else:
        print("No process has been selected in Continue selection of process")
    # CountElements()
    # AlphabetizeElements()
    # eci_1 = cb_eci_1.get()
    # print("Process selected is " , process_selected)
    # print('eci_1 = ', eci_1)
    # print("Pressed Continue button")

def Set_default_T_and_P():
    print("1287 In Set_default_T_and_P function")

def Balance_Equation():
    print("1290 In Set_default_T_and_P function")
    be = ""
    print("Started Balance_Equation")
    e_Explanation.insert(END, "Started Balance_Equation")
    e_Explanation.insert(END, '\n')
    e_Explanation.insert(END, "Step 1: ")
    if cb_eci_1.get() != "":
        be = cb_eci_1.get()
        print("cb_eci_1 is ", be)
        #e_Explanation.insert(END, cb_eci_1.get())
    if cb_eci_2.get() != "":
        be = be + " + " + cb_eci_2.get()
        print("cb_eci_2 is ", be)
        #e_Explanation.insert(END, be)
    if cb_eci_3.get() != "":
        be = be + " + " + cb_eci_3.get()
        print("cb_eci_3 is ", be)
        #e_Explanation.insert(END, be)
    if cb_eci_4.get() != "":
        be = be + " --> " + cb_eci_4.get()
        print("cb_eci_4 is ", be)
        #e_Explanation.insert(END, be)
    if cb_eci_5.get() != "":
        be = be + " + " + cb_eci_5.get()
        print("cb_eci_5 is ", be)
        #e_Explanation.insert(END, be)
    if cb_eci_6.get() != "":
        be = be + " + " + cb_eci_6.get()
        print("cb_eci_6 is ", be)
    e_Explanation.insert(END, be)

def calculate():
    print("1322 In calculate function")
    ''' A step toward performing general chemistry related calculations.
    There will be many calculations done by the program.
    They will be separated into separate functions as they are developed.'''
    #Message.config(font, titlefont)
    #showinfo.__setattr__(font, 'Helvetica 12') # Doesn't work
    #mb.Dialog.show(title=None, message="To calculate eci variable, senter an element type and symbol and a mole quantity.")
    #showinfo(title=None, message="To calculate eci variables, enter an element type and symbol and a mole quantity.")
    #check_entry_changes()
    #calculate_eci_variables()

def setClassItem(eventObject): # This function appears to be redundant.
    print("1334 In setClassItem function")

    ''' If eci_1 or eci_2 are elements, set their quantity and name variables. '''
    #e_Explanation.insert(tk.END, "setClassItem process entered\n")
    # print("setClassItem process entered")
    '''eci_1 = cb_eci_1.get()
    # print('eci_1 is', eci_1)
    # *** The following works!
    if cb_1_type == 'elements':
        eci_temp_1_qty = db[eci_1]['mass']
        eci_1_name = db[eci_1]['name']
        e_Explanation.insert(END, "db[eci_1]['mass'] is ", eci_temp_1_qty, '\n')
        print("db[eci_1]['mass'] is ", eci_temp_1_qty)
        print("db[eci_1]['name'] is ", eci_1_name)
    elif cb_1_type == 'compounds':
        eci_1 = cb_eci_1.get()
        eci_1_name = c_db[eci_1]['name']
        print('eci_1 = ', eci_1)
        print("In setClassItem at elif compounds")
        '''
'''
r1 = dict(name= 'Record 1', id= 1, compound= 'None', process= 'None', major_process= 'None', minor_process= 'None', environment= 'None',
          equipment = "", energy_type = "", energy_amount = "", catalyst = "", side_effects = "", by_products = "",
          variables = "", variable_values = "", explanation = "",
          eci_1_type = "", eci_1_formula= "", eci_1_name = "", eci_1_units = "", eci_1_qty = "", eci_1_M_qty = "", eci_1_valence = "",
          eci_1_temp_display_units = "", eci_1_temp_calc_units = "", eci_1_temp_display_qty = "", eci_1_temp_calc_qty = "",
          eci_1_press_display_units = "", eci_1_press_calc_units = "", eci_1_press_display_qty = "", eci_1_press_calc_qty = "",
          eci_2_type = "", eci_3_type = "", eci_4_type = "", eci_5_type = "", eci_6_type = "")
'''

def setElementInitialVariables(cb_number):
    print('1365 Entered setElementInitialVariables. cb_number is ', cb_number)
    if cb_number == "cb_1_type":
        print('Entered setElementInitialVariables if cb_number == cb_1_type statement.')
        dbr['R1']['eci_1_formula'] = cb_eci_1.get()
        print("dbr['R1']['eci_1_formula'] is ", dbr['R1']['eci_1_formula'])
        dbr['R1']['eci_1_name'] = cb_eci_1_N.get()
        print("dbr['R1']['eci_1_name'] is ", dbr['R1']['eci_1_name'])
        ''' The following works to set units to grams.'''
        cb_eci_1_units.set('grams')
        #cb_eci_1_units.set(eci_1_units)
        dbr['R1']['eci_1_units'] = 'grams'
        ''' Initial value of qty is the selected element atomic mass in grams. '''
        dbr['R1']['eci_1_qty'] = db[eci_1.get()]['mass']
        print("1295 dbr['R1']['eci_1_qty'] is ", dbr['R1']['eci_1_qty'])
        ''' Get the atomic mass of the selected element. then set e_eci_1_qty equal to it. '''
        eci_1_M_qty = getdouble(e_eci_1_M_qty.get())

        ''' ********** eci_1 gives user a PVAR. Use eci_1.get() to get the actual value of eci_1 '''
        #print('eci_1 is ', eci_1.get())
        eci_1_mass = db[eci_1.get()]['mass']    #db[eci_1]['mass']
        #print('eci_1_M_qty is ', eci_1_M_qty)
        print('1303 eci_1_mass is ', eci_1_mass) #eci_1.get['mass'])
        eci_1_qty = eci_1_mass  #db[eci_1.get()]['eci_1_mass']
        ''' ************************************************************ '''
        ''' The following works to inset the (atomic mass) into the quantity entry widget! '''
        ''' But, it only works if an element symbol is selected; not if the name is selected. '''
        e_eci_1_qty.delete(0, tk.END)
        e_eci_1_qty.insert(0, eci_1_qty)   #eci_1_mass)
        dbr['R1']['eci_1_qty'] = e_eci_1_qty.get()
        print("dbr['R1']['eci_1_qty'] is ", dbr['R1']['eci_1_qty'])

def setSelectedItemInitialVariables(cb_type, type):
        """
        Use this function to set all the variables associated with a selected item.
        For example, set the atomic number or molecular mass,and display the appropriate values.
        such as e_eci_1_qty = eci_1_mass -- find and replace with the appropriate db value
        """
        print("1400 Entered setSelectedItemVariables ", cb_type,  type)
        cb_1_type = cb_Select_CB1.get()
        cb_2_type = cb_Select_CB2.get()
        cb_3_type = cb_Select_CB3.get()

        ''' I should add an additional criteria to check so all statements don't run extra times. '''
        ''' If the type is elements and the formula is different, process it; otherwise pass.'''
        if cb_1_type == 'elements' and dbr['R1']['eci_1_formula'] != cb_eci_1.get(): #and e_eci_1_qty == 0.0:  # and cb_2_type == '' and cb_3_type == '':    #cb_type == cb_1_type and type == 'elements':
            #setElementInitialVariables(cb_1_type)
            print('Entered setSelectedItemVariables, cb_1_type == elements')
            print('e_eci_1_qty is ', e_eci_1_qty.get())
            dbr['R1']['eci_1_formula'] = cb_eci_1.get()
            print("dbr['R1']['eci_1_formula'] is ", dbr['R1']['eci_1_formula'])
            dbr['R1']['eci_1_name'] = cb_eci_1_N.get()
            print("dbr['R1']['eci_1_name'] is ", dbr['R1']['eci_1_name'])
            ''' The following works to set units to grams.'''
            cb_eci_1_units.set('grams')
            #cb_eci_1_units.set(eci_1_units)
            dbr['R1']['eci_1_units'] = 'grams'
            ''' Initial value of qty is the selected element atomic mass in grams. '''
            dbr['R1']['eci_1_qty'] = db[eci_1.get()]['mass']
            print("1337 dbr['R1']['eci_1_qty'] is ", dbr['R1']['eci_1_qty'])
            ''' Get the atomic mass of the selected element. then set e_eci_1_qty equal to it. '''
            eci_1_M_qty = getdouble(e_eci_1_M_qty.get())

            ''' ********** eci_1 gives user a PVAR. Use eci_1.get() to get the actual value of eci_1 '''
            #print('eci_1 is ', eci_1.get())
            eci_1_mass = db[eci_1.get()]['mass']    #db[eci_1]['mass']
            #print('eci_1_M_qty is ', eci_1_M_qty)
            print('1345 eci_1_mass is ', eci_1_mass) #eci_1.get['mass'])
            eci_1_qty = eci_1_mass  #db[eci_1.get()]['eci_1_mass']
            ''' ************************************************************ '''
            ''' The following works to inset the (atomic mass) into the quantity entry widget! '''
            ''' But, it only works if an element symbol is selected; not if the name is selected. '''
            e_eci_1_qty.delete(0, tk.END)
            e_eci_1_qty.insert(0, eci_1_qty)   #eci_1_mass)
            e_eci_1_M_qty.delete(0, tk.END)
            e_eci_1_M_qty.insert(0, 1.0)

        if cb_2_type == 'elements': # and cb_2_type == 'elements':
            print('Entered setSelectedItemVariables, cb_2_type == elements')
            dbr['R1']['eci_2_formula'] = cb_eci_2.get()
            print("dbr['R1']['eci_2_formula'] is ", dbr['R1']['eci_2_formula'])
            dbr['R1']['eci_2_name'] = cb_eci_2_N.get()
            print("dbr['R1']['eci_2_name'] is ", dbr['R1']['eci_2_name'])
            cb_eci_2_units.set('grams')
            dbr['R1']['eci_2_units'] = 'grams'
            dbr['R1']['eci_2_qty'] = db[eci_2.get()]['mass']
            print("121364 dbr['R1']['eci_2_qty'] is ", dbr['R1']['eci_2_qty'])
            ''' Get the atomic mass of the selected element. then set e_eci_3_qty equal to it. '''
            #eci_2_M_qty = getdouble(e_eci_2_M_qty.get())
            eci_2_mass = db[eci_2.get()]['mass']    #db[eci_1]['mass']
            #print('eci_2_M_qty is ', eci_2_M_qty)
            print('1369 eci_2_mass is ', eci_2_mass) #eci_1.get['mass'])
            eci_2_qty = eci_2_mass  #db[eci_1.get()]['eci_1_mass']
            ''' ************************************************************ '''
            ''' The following works to inset the (atomic mass) into the quantity entry widget! '''
            ''' But, it only works if an element symbol is selected; not if the name is selected. '''
            e_eci_2_qty.delete(0, tk.END)
            e_eci_2_qty.insert(0, eci_2_qty)
            e_eci_2_M_qty.delete(0, tk.END)
            e_eci_2_M_qty.insert(0, 1.0)

        if cb_3_type == 'elements':
            #setElementInitialVariables(cb_1_type)
            print('Entered setSelectedItemVariables, cb_3_type == elements')
            dbr['R1']['eci_3_formula'] = cb_eci_3.get()
            print("dbr['R1']['eci_3_formula'] is ", dbr['R1']['eci_3_formula'])
            dbr['R1']['eci_3_name'] = cb_eci_3_N.get()
            print("dbr['R1']['eci_3_name'] is ", dbr['R1']['eci_3_name'])
            ''' The following works to set units to grams.'''
            cb_eci_3_units.set('grams')
            #cb_eci_1_units.set(eci_1_units)
            dbr['R1']['eci_3_units'] = 'grams'
            ''' Initial value of qty is the selected element atomic mass in grams. '''
            dbr['R1']['eci_3_qty'] = db[eci_3.get()]['mass']
            print("1392 dbr['R1']['eci_3_qty'] is ", dbr['R1']['eci_3_qty'])
            ''' Get the atomic mass of the selected element. then set e_eci_3_qty equal to it. '''
            eci_3_M_qty = getdouble(e_eci_3_M_qty.get())

            ''' ********** eci_1 gives user a PVAR. Use eci_1.get() to get the actual value of eci_1 '''
            #print('eci_1 is ', eci_1.get())
            eci_3_mass = db[eci_3.get()]['mass']    #db[eci_1]['mass']
            #print('eci_1_M_qty is ', eci_1_M_qty)
            print('1400 eci_3_mass is ', eci_3_mass) #eci_1.get['mass'])
            eci_3_qty = eci_3_mass  #db[eci_1.get()]['eci_1_mass']
            ''' ************************************************************ '''
            ''' The following works to inset the (atomic mass) into the quantity entry widget! '''
            ''' But, it only works if an element symbol is selected; not if the name is selected. '''
            e_eci_3_qty.delete(0, tk.END)
            e_eci_3_qty.insert(0, eci_3_qty)
            e_eci_3_M_qty.delete(0, tk.END)
            e_eci_3_M_qty.insert(0, 1.0)

            ''' 
            Use the following print statements as needed later. They are currently used above while developing
            the program.
            '''
            #print("dbr['R1']['eci_1_type'] = ", dbr['R1']['eci_1_type'])
            #print("dbr['R1']['eci_1_formula'] is ", dbr['R1']['eci_1_formula'])
            #print("dbr['R1']['eci_1_name'] is ", dbr['R1']['eci_1_name'])
            ''' Shouldn't need the following anymore. Delete when confirmed.'''
            #print("eci_db['eci_1']['name'] is ", eci_db['eci_1']['name'])
            #print("eci_1_d['eci'] is ", eci_1_d['eci'])
            #print("eci_1_d['name'] is ", eci_1_d['name'])
            #dbr['R1']['mass'] = db[eci_1]['mass']
            #dbr['R1']['valence'] = db[eci_1]['valence']
            #eci_d['eci_1']['mass'] = db[eci_1]['mass']
            #eci_d['eci_1']['valence'] = db[eci_1]['valence']
            #e_eci_1_M_qty.delete(0, END)
            #e_eci_1_M_qty.insert(0, 1)


def setSelectedItemName(ComboboxSelected):
    print('1513 Entered setSelectedItemName ')   # ComboboxSelected provides "<VirtualEvent event x=0 y=0>"
    cb_1_type = cb_Select_CB1.get()
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()
    cb_4_type = cb_Select_CB4.get()
    cb_5_type = cb_Select_CB5.get()
    cb_6_type = cb_Select_CB6.get()
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    eci_3 = cb_eci_3.get()
    eci_4 = cb_eci_4.get()
    eci_5 = cb_eci_5.get()
    eci_6 = cb_eci_6.get()
    eci_1_name = cb_eci_1_N.get()
    eci_2_name = cb_eci_2_N.get()
    eci_3_name = cb_eci_3_N.get()
    eci_4_name = cb_eci_4_N.get()
    eci_5_name = cb_eci_5_N.get()
    eci_6_name = cb_eci_6_N.get()
    # print("eci_1_name is ", eci_1_name)

    if cb_1_type == 'elements':
        try:
            if not eci_1_name == db[eci_1]['name']:
                cb_eci_1_N.set(db[eci_1]['name'])   # This works
                setSelectedItemInitialVariables('cb_1_type', 'elements')
                #eci_1_d['eci'] = cb_eci_1.get()
                #eci_1_d['name'] = db[eci_1]['name'] #cb_eci_1_N.get()
                #eci_d['eci_1']['eci'] = eci_1
                #eci_d['eci_1']['name'] = db[eci_1]['name'] #eci_1_name
                #print("eci_db['eci_1']['eci'] is ", eci_db['eci_1']['eci'])
                #print("eci_db['eci_1']['name'] is ", eci_db['eci_1']['name'])
                #print("eci_1_d['eci'] is ", eci_1_d['eci'])
                #print("eci_1_d['name'] is ", eci_1_d['name'])
        except KeyError:
            cb_eci_1_N.set("not a valid key")
    elif cb_1_type == 'compounds':
        try:
            if not eci_1_name == c_db[eci_1]['name']:
                cb_eci_1_N.set(c_db[eci_1]['name'])
                eci_1_d['eci'] = cb_eci_1.get()
                eci_1_d['name'] = eci_1_name
        except KeyError:
            cb_eci_1_N.set("not a valid key")
    elif cb_1_type == 'ions':
        try:
            if not eci_1_name == i_db[eci_1]['name']:
                cb_eci_1_N.set(i_db[eci_1]['name'])
                eci_1_d['eci'] = cb_eci_1.get()
                eci_1_d['name'] = eci_1_name
        except KeyError:
            cb_eci_1_N.set("not a valid key")
    elif cb_1_type == 'acids':
        print("The structure for acids has not been written.")
    elif cb_1_type == 'bases':
        print("The structure for bases has not been written.")
    elif cb_1_type == 'polyatomic':
        print("The structure for polyatomic has not been written.")

    if cb_2_type == 'elements':
        try:
            if not eci_2_name == db[eci_2]['name']:
                cb_eci_2_N.set(db[eci_2]['name'])
                setSelectedItemInitialVariables('cb_2_type', 'elements')
                #eci_2_d['eci'] = cb_eci_2.get()
                #eci_2_d['name'] = eci_2_name
        except KeyError:
            cb_eci_2_N.set("not a valid key")
    elif cb_2_type == 'compounds':
        try:
            if not eci_2_name == c_db[eci_2]['name']:
                cb_eci_2_N.set(c_db[eci_2]['name'])
                #eci_2_d['eci'] = cb_eci_2.get()
                #eci_2_d['name'] = eci_2_name
        except KeyError:
            cb_eci_2_N.set("not a valid key")
    elif cb_2_type == 'ions':
        try:
            if not eci_2_name == i_db[eci_2]['name']:
                cb_eci_2_N.set(i_db[eci_2]['name'])
                eci_2_d['eci'] = cb_eci_2.get()
                eci_2_d['name'] = eci_2_name
        except KeyError:
            cb_eci_2_N.set("not a valid key")
    if cb_3_type == 'elements':
        try:
            if not eci_3_name == db[eci_3]['name']:
                cb_eci_3_N.set(db[eci_3]['name'])
                setSelectedItemInitialVariables('cb_3_type', 'elements')
                #eci_3_d['eci'] = cb_eci_3.get()
                #eci_3_d['name'] = eci_3_name
        except KeyError:
            cb_eci_3_N.set("not a valid key")
    elif cb_3_type == 'compounds':
        try:
            if not eci_3_name == c_db[eci_3]['name']:
                cb_eci_3_N.set(c_db[eci_3]['name'])
                eci_3_d['eci'] = cb_eci_3.get()
                eci_3_d['name'] = eci_3_name
        except KeyError:
            cb_eci_3_N.set("not a valid key")
    elif cb_3_type == 'ions':
        try:
            if not eci_3_name == i_db[eci_3]['name']:
                cb_eci_3_N.set(i_db[eci_3]['name'])
                eci_3_d['eci'] = cb_eci_3.get()
                eci_3_d['name'] = eci_3_name
        except KeyError:
            cb_eci_3_N.set("not a valid key")
    if cb_4_type == 'elements':
        try:
            if not eci_4_name == db[eci_4]['name']:
                cb_eci_4_N.set(db[eci_4]['name'])
                eci_4_d['eci'] = cb_eci_4.get()
                eci_4_d['name'] = eci_4_name
        except KeyError:
            cb_eci_4_N.set("not a valid key")
    elif cb_4_type == 'compounds':
        try:
            if not eci_4_name == c_db[eci_4]['name']:
                cb_eci_4_N.set(c_db[eci_4]['name'])
                eci_4_d['eci'] = cb_eci_4.get()
                eci_4_d['name'] = eci_4_name
        except KeyError:
            cb_eci_4_N.set("not a valid key")
    elif cb_4_type == 'ions':
        try:
            if not eci_4_name == i_db[eci_4]['name']:
                cb_eci_4_N.set(i_db[eci_4]['name'])
                eci_4_d['eci'] = cb_eci_4.get()
                eci_4_d['name'] = eci_4_name
        except KeyError:
            cb_eci_4_N.set("not a valid key")
    if cb_5_type == 'elements':
        try:
            if not eci_5_name == db[eci_5]['name']:
                cb_eci_5_N.set(db[eci_5]['name'])
                eci_5_d['eci'] = cb_eci_5.get()
                eci_5_d['name'] = eci_5_name
        except KeyError:
            cb_eci_5_N.set("not a valid key")
    elif cb_5_type == 'compounds':
        try:
            if not eci_5_name == c_db[eci_5]['name']:
                cb_eci_5_N.set(c_db[eci_5]['name'])
                eci_5_d['eci'] = cb_eci_5.get()
                eci_5_d['name'] = eci_5_name
        except KeyError:
            cb_eci_5_N.set("not a valid key")
    elif cb_5_type == 'ions':
        try:
            if not eci_5_name == i_db[eci_5]['name']:
                cb_eci_5_N.set(i_db[eci_5]['name'])
                eci_5_d['eci'] = cb_eci_5.get()
                eci_5_d['name'] = eci_5_name
        except KeyError:
            cb_eci_5_N.set("not a valid key")
    if cb_6_type == 'elements':
        try:
            if not eci_6_name == db[eci_6]['name']:
                cb_eci_6_N.set(db[eci_6]['name'])
                eci_6_d['eci'] = cb_eci_6.get()
                eci_6_d['name'] = eci_6_name
        except KeyError:
            cb_eci_6_N.set("not a valid key")
    elif cb_6_type == 'compounds':
        try:
            if not eci_6_name == c_db[eci_6]['name']:
                cb_eci_6_N.set(c_db[eci_6]['name'])
                eci_6_d['eci'] = cb_eci_6.get()
                eci_6_d['name'] = eci_6_name
        except KeyError:
            cb_eci_6_N.set("not a valid key")
    elif cb_6_type == 'ions':
        try:
            if not eci_6_name == i_db[eci_6]['name']:
                cb_eci_6_N.set(i_db[eci_6]['name'])
                eci_6_d['eci'] = cb_eci_6.get()
                eci_6_d['name'] = eci_6_name
        except KeyError:
            cb_eci_6_N.set("not a valid key")
    else:
        pass  # print('In else clause of setSelectedItemName.')


def setSelectedItemFormula(ComboboxSelected):
    print('1699 Entered setSelectedItemFormula ')
    eci_1_N = cb_eci_1_N.get()
    eci_2_N = cb_eci_2_N.get()
    eci_3_N = cb_eci_3_N.get()
    eci_4_N = cb_eci_4_N.get()
    eci_5_N = cb_eci_5_N.get()
    eci_6_N = cb_eci_6_N.get()
    cb_1_type = cb_Select_CB1.get()
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()
    cb_4_type = cb_Select_CB4.get()
    cb_5_type = cb_Select_CB5.get()
    cb_6_type = cb_Select_CB6.get()
    ''' If the name in the name combobox is not the name associated with the selected element, update the name.'''
    if cb_1_type == 'elements':
        if not eci_1 == element_names_Dict[cb_eci_1_N.get()]:
            cb_eci_1.set(element_names_Dict[cb_eci_1_N.get()])
    elif cb_1_type == 'compounds':
        if not eci_1 == compound_names_dict[cb_eci_1_N.get()]:
            cb_eci_1.set(compound_names_dict[cb_eci_1_N.get()])
        else:
            print('eci_1 is already correct and doesn\'t need to be reset')
    elif cb_1_type == 'ions':
        if not eci_1 == ion_names_dict[cb_eci_1_N.get()]:
            cb_eci_1.set(ion_names_dict[cb_eci_1_N.get()])
    if cb_2_type == 'elements':
        if not eci_2 == element_names_Dict[cb_eci_2_N.get()]:
            cb_eci_2.set(element_names_Dict[cb_eci_2_N.get()])
    elif cb_2_type == 'compounds':
        if not eci_2 == compound_names_dict[cb_eci_2_N.get()]:
            cb_eci_2.set(compound_names_dict[cb_eci_2_N.get()])
    elif cb_2_type == 'ions':
        if not eci_2 == ion_names_dict[cb_eci_2_N.get()]:
            cb_eci_2.set(ion_names_dict[cb_eci_2_N.get()])
    if cb_3_type == 'elements':
        if not eci_3 == element_names_Dict[cb_eci_3_N.get()]:
            cb_eci_3.set(element_names_Dict[cb_eci_3_N.get()])
    elif cb_3_type == 'compounds':
        if not eci_3 == compound_names_dict[cb_eci_3_N.get()]:
            cb_eci_3.set(compound_names_dict[cb_eci_3_N.get()])
    elif cb_3_type == 'ions':
        if not eci_3 == ion_names_dict[cb_eci_3_N.get()]:
            cb_eci_3.set(ion_names_dict[cb_eci_3_N.get()])
    if cb_4_type == 'elements':
        if not eci_4 == element_names_Dict[cb_eci_4_N.get()]:
            cb_eci_4.set(element_names_Dict[cb_eci_4_N.get()])
    elif cb_4_type == 'compounds':
        if not eci_4 == compound_names_dict[cb_eci_4_N.get()]:
            cb_eci_4.set(compound_names_dict[cb_eci_4_N.get()])
    elif cb_4_type == 'ions':
        if not eci_4 == ion_names_dict[cb_eci_4_N.get()]:
            cb_eci_4.set(ion_names_dict[cb_eci_4_N.get()])
    if cb_5_type == 'elements':
        if not eci_5 == element_names_Dict[cb_eci_5_N.get()]:
            cb_eci_5.set(element_names_Dict[cb_eci_5_N.get()])
    elif cb_5_type == 'compounds':
        if not eci_5 == compound_names_dict[cb_eci_5_N.get()]:
            cb_eci_5.set(compound_names_dict[cb_eci_5_N.get()])
    elif cb_5_type == 'ions':
        if not eci_5 == ion_names_dict[cb_eci_5_N.get()]:
            cb_eci_5.set(ion_names_dict[cb_eci_5_N.get()])
    if cb_6_type == 'elements':
        if not eci_6 == element_names_Dict[cb_eci_6_N.get()]:
            cb_eci_6.set(element_names_Dict[cb_eci_6_N.get()])
    elif cb_6_type == 'compounds':
        if not eci_6 == compound_names_dict[cb_eci_6_N.get()]:
            cb_eci_6.set(compound_names_dict[cb_eci_6_N.get()])
    elif cb_6_type == 'ions':
        if not eci_6 == ion_names_dict[cb_eci_6_N.get()]:
            cb_eci_6.set(ion_names_dict[cb_eci_6_N.get()])


def eci_units_selected(*arg):
    print('1772 Entered eci_units_selected ')
    ''' If gas units are selected, the user needs to fill in temperature and pressure
    units and amounts. This procedure sets default values.
    The user can reset the displayed units and quantities, but they will be converted into
    the units and quantities actually used to calculate quantities used by the program.  '''
    print("1764 In process eci_units_selected")
    #print("cb_eci_1_units.get() is ", cb_eci_1_units.get())
    eci_1 = cb_eci_1.get()
    dbr['R1']['eci_1_formula'] = eci_1
    print("1812 dbr['R1']['eci_1_formula'] is ", dbr['R1']['eci_1_formula'])
    eci_1_units = cb_eci_1_units.get()
    eci_2_units = cb_eci_2_units.get()
    eci_3_units = cb_eci_3_units.get()
    eci_4_units = cb_eci_4_units.get()
    eci_5_units = cb_eci_5_units.get()
    dbr['R1']['eci_1_display_units'] = cb_eci_1_units.get()
    dbr['R1']['eci_1_calc_units'] = cb_eci_1_units.get()
    print("1820 dbr['R1']['eci_1_display_units'] ", dbr['R1']['eci_1_display_units']) #dbr['R1']['eci_1_display_units'])
    print("1821 dbr['R1']['eci_1_calc_units'] ", dbr['R1']['eci_1_calc_units'])
    #r1['eci_2']['display_units'] = cb_eci_2_units.get()
    #r1['eci_3']['display_units'] = cb_eci_3_units.get()
    #r1['eci_4']['display_units'] = cb_eci_4_units.get()
    #r1['eci_5']['display_units'] = cb_eci_5_units.get()
    #r1['eci_6']['display_units'] = cb_eci_6_units.get()
    #eci_d['eci_1']['display_units'] = cb_eci_1_units.get()
    #ci_d['eci_2']['display_units'] = cb_eci_2_units.get()
    #eci_d['eci_3']['display_units'] = cb_eci_3_units.get()
    #eci_d['eci_4']['display_units'] = cb_eci_4_units.get()
    #eci_d['eci_5']['display_units'] = cb_eci_5_units.get()
    #eci_d['eci_6']['display_units'] = cb_eci_6_units.get()
    if eci_1_units == 'liters(l)' or eci_1_units == 'ml(l)' or eci_1_units == 'liters(g)' or eci_1_units == 'ml(g)':    #liters(l) liters(g) ml(l) ml(g
        dbr['R1']['eci_1_display_units'] = eci_1_units
        dbr['R1']['eci_1_calc_units'] = eci_1_units
        print("1833 eci_1_units are ", eci_1_units) # == 'liters(g)')
        print("1834 dbr['R1']['eci_1_display_units'] ", dbr['R1']['eci_1_display_units'])
        if cb_1_Temp_Units.get() == "":
            eci_1_temp_units = cb_1_Temp_Units.set('C')
            e_Temp_Qty_1.delete(0, tk.END)
            e_Temp_Qty_1.insert(0, 0)
        elif cb_1_Temp_Units.get() == 'C':
            e_Temp_Qty_1.delete(0, tk.END)
            e_Temp_Qty_1.insert(0, 0)
        elif cb_1_Temp_Units.get() == 'K':
            e_Temp_Qty_1.delete(0, tk.END)
            e_Temp_Qty_1.insert(0, 273.15)
        elif cb_1_Temp_Units.get() == 'F':
            e_Temp_Qty_1.delete(0, tk.END)
            e_Temp_Qty_1.insert(0, -32)

        # initialize at 0 degrees C -- stp
        #print('1797 e_Press_Qty_1.get() is ', e_Press_Qty_1.get())
        if cb_1_Press_Units.get() == "":
            eci_1_press_units = cb_1_Press_Units.set('atm')
            e_Press_Qty_1.delete(0, tk.END)
            e_Press_Qty_1.insert(0, 1.0) # initialize at 1 atm -- stp
            e_eci_1_qty.delete(0, tk.END)
            e_eci_1_qty.insert(0, 22.4)   #eci_1_mass)
            e_eci_1_M_qty.delete(0, tk.END)
            e_eci_1_M_qty.insert(0, 1.0)
        elif cb_1_Press_Units.get() == "atm":
            #eci_1_press_units = cb_1_Press_Units.set('atm')
            e_Press_Qty_1.delete(0, tk.END)
            e_Press_Qty_1.insert(0, 1.0) # initialize at 1 atm -- stp
            e_eci_1_qty.delete(0, tk.END)
            e_eci_1_qty.insert(0, 22.4)   #eci_1_mass)
            e_eci_1_M_qty.delete(0, tk.END)
            e_eci_1_M_qty.insert(0, 1.0)

'''
    # elif not eci_1_units == 'liters(g)' and not eci_1_units == 'ml(g)':
    #     print('cb_eci_1_units are ', eci_1_units)
    if eci_2_units == 'liters(l)' or eci_2_units == 'ml(l)' or eci_2_units == 'liters(g)' or eci_2_units == 'ml(g)':
        if cb_2_Temp_Units.get() == "":
            eci_2_temp_units = cb_2_Temp_Units.set('C')
        if cb_2_Press_Units.get() == "":
            eci_2_press_units = cb_2_Press_Units.set('ATM')
    if eci_3_units == 'liters(l)' or eci_3_units == 'ml(l)' or eci_3_units == 'liters(g)' or eci_3_units == 'ml(g)':
        if cb_3_Temp_Units.get() == "":
            eci_3_temp_units = cb_3_Temp_Units.set('C')
        if cb_3_Press_Units.get() == "":
            eci_3_press_units = cb_3_Press_Units.set('ATM')
    if eci_4_units == 'liters(l)' or eci_4_units == 'ml(l)' or eci_4_units == 'liters(g)' or eci_4_units == 'ml(g)':
        if cb_4_Temp_Units.get() == "":
            eci_4_temp_units = cb_4_Temp_Units.set('C')
        if cb_4_Press_Units.get() == "":
            eci_4_press_units = cb_4_Press_Units.set('ATM')
    if eci_5_units == 'liters(l)' or eci_5_units == 'ml(l)' or eci_5_units == 'liters(g)' or eci_5_units == 'ml(g)':
        if cb_5_Temp_Units.get() == "":
            eci_5_temp_units = cb_5_Temp_Units.set('C')
        if cb_4_Press_Units.get() == "":
            eci_5_press_units = cb_5_Press_Units.set('ATM')
    if eci_6_units == 'liters(l)' or eci_6_units == 'ml(l)' or eci_6_units == 'liters(g)' or eci_6_units == 'ml(g)':
        if cb_6_Temp_Units.get() == "":
            eci_6_temp_units = cb_6_Temp_Units.set('C')
        if cb_6_Press_Units.get() == "":
            eci_6_press_units = cb_6_Press_Units.set('ATM')
    eci_d['eci_1']['display_temp_units'] = cb_1_Temp_Units.get()
    eci_d['eci_2']['display_temp_units'] = cb_2_Temp_Units.get()
    eci_d['eci_3']['display_temp_units'] = cb_3_Temp_Units.get()
    eci_d['eci_4']['display_temp_units'] = cb_4_Temp_Units.get()
    eci_d['eci_5']['display_temp_units'] = cb_5_Temp_Units.get()
    eci_d['eci_6']['display_temp_units'] = cb_6_Temp_Units.get()
    eci_d['eci_1']['display_press_units'] = cb_1_Press_Units.get()
    eci_d['eci_2']['display_press_units'] = cb_2_Press_Units.get()
    eci_d['eci_3']['display_press_units'] = cb_3_Press_Units.get()
    eci_d['eci_4']['display_press_units'] = cb_4_Press_Units.get()
    eci_d['eci_5']['display_press_units'] = cb_5_Press_Units.get()
    eci_d['eci_6']['display_press_units'] = cb_6_Press_Units.get()
    #print("eci_db['eci_1']['display_temp_units'] are ", eci_db['eci_1']['display_temp_units'])
    #print("eci_db['eci_1']['display_press_units'] are ", eci_db['eci_1']['display_press_units'])
'''
def calculate_eci_variables():
    print('1871 In process calculate_eci_variables')
    '''
    A step toward calculating variables associated with an eci.
    This one simply gets an element symbol, retrieves the atomic mass,
    and the mole quantity, calculates the quantity in grams, and
    inserts that quantity into the eci quantity entry box.
    '''
    '''msg_Calculate_eci_variables = Label(text=showinfo(title=None, message=None, **options), enter an element type and symbol and a mole quantity.")
    msg_Calculate_eci_variables.config(font=labelfont)
    msg_Calculate_eci_variables.grid(row=8, column=0)
    '''
    ''' What will standard calculation units be? Set them in the eci frame dictionary.
    If a temp or press units or quantity changes, change the value in the eci frame dictionary.
    If there is a mole quantity, assume it is correct and change the regular quantity.
    Implement controlled changes in mole and regular quantities. For example,if a mole quantity
    changes, calculate the regular quantity. If that quantity already exists in the quantity box,
    do not change it. Otherwise change it. Likewise, if the mole quantity is the same, do not change it.
    After each change, the values in the dicionary need to be set. Check the logic, it may be better
    to verify changes in the dictionary values and then change the mole and regular quantities
    rather than delegating the change control to the widgets. Widgets changes update the directory
    and the directory updates the widgets.
    '''
    ''' The following process currently only works for eci_1'''
    #check_entry_changes()
    #print('In process calculate_eci_variables after check_entry_changes')
    #eci_1 = cb_eci_1.get()
    #print('eci_1 is ', eci_1)
    #eci_1_M_qty = e_eci_1_M_qty.get()
    ''' e_eci_1_qty.insert(0, eci_1_M_qty) WORKS!!! '''
    #print('eci_1_M_qty is ', eci_1_M_qty)
    #eci_1_units = cb_eci_1_units.get()
    #print('eci_1_units are ', eci_1_units)

    if eci_1_units == 'liters(l)' or eci_1_units == 'liters(g)' or eci_1_units == 'ml(l)' or eci_1_units == 'ml(g)':
            #and not eci_1_M_qty == 0.0:
        pvnrt(eci, item)

    #else:
    #if eci_1_units == 'grams' and not eci_1_M_qty == "":
    ''' eci_1_mass = DoubleVar() '''
    #eci_1_mass = getdouble(db[eci_1]['mass'])
    #eci_1_mass = db[eci_1]['mass'].get()  #eci_1('mass')   #
    eci_1_M_qty = getdouble(e_eci_1_M_qty.get())
    #print('eci_1_mass = ', getdouble(db[eci_1]['mass']))   #eci_1('mass'))    #eci_1_mass)
    print('eci_1_M_qty = ', getdouble(e_eci_1_M_qty.get()))
    #m_mass = eci_1_M_qty * 26    #getdouble(db[eci_1]['mass'])  #26   #eci_1_mass getdouble(db[eci_1]['mass'])
    #e_eci_1_qty.delete(0, END)
    #e_eci_1_qty.insert(0, m_mass)
    #e_Explanation.insert(END, m_mass)
    #print('m_mass is ', m_mass)

    #if not eci_1_M_qty == "":  ''' Have not yet incorporated temp and press into calculate

    #    eci_1_temp_units = cb_1_Temp_Units.get()
    #    print('eci_1_temp_units are ', eci_1_temp_units)
    #    eci_1_press_units_units = cb_1_Press_Units.get()
    #    print('eci_1_press_units_units are ', eci_1_press_units_units)
        #eci_1_temp_units = cb_1_Temp_Units.get()
        #e_Temp_Qty_1.delete(0, END)
        #e_Temp_Qty_1.insert(0, 288)
        #eci_1_press_units = "ATM"
        #e_Press_Qty_1.delete(0, END)
        #e_Press_Qty_1.insert(0, 0.967)
        # vol_from_prt()    ''' Not yet ready to incorporate gas calculations into calculate process
#pdb.set_trace()
def mole_mass_change(eci, item): #pvnrt_1
    """ Procedure pvnrt makes adjustmenst to changes in eci_1 values.
    I can't just adjust a value or units, I need to retrieve all the other units and values
    in order to determine what changes to make. For example, to implement PV = nRT,
    the program needs to retrieve all the values and units associated with a change.
    These changes will need to be cascaded due to other programatic changes.
    For example, if the process is 'Synthesis', and the compound changes the number of moles
    of an elemeent, that changes needs to be made. And it needs to progress from moles to
    whatever the correct units are for that element -- e.g. liters of gas. """
    print('1944 mole_mass_change event procedure called.', eci, item)
    current_eci_1_units = cb_eci_1_units.get()
    dbr['R1']['eci_1_units'] = current_eci_1_units
    current_eci_2_units = cb_eci_2_units.get()
    dbr['R1']['eci_2_units'] = current_eci_2_units
    current_eci_3_units = cb_eci_3_units.get()
    dbr['R1']['eci_3_units'] = current_eci_3_units
    print('1992 current_eci_1_units is ', current_eci_1_units)
    print("1991 dbr['R1']['eci_1_units'] is ", dbr['R1']['eci_1_units'])
    if dbr['R1']['eci_1_units'] == 'grams':
        if item == "qty":
            ''' I can't just adjust the eci_1_qty, I need to determine what it should be based on units.
            Since units are in grams, I need to retrieve the element atomic mass and use it for calculations.'''
            print("1829 dbr['R1']['eci_1_units'] == ", dbr['R1']['eci_1_units'])
            dbr['R1']['eci_1_qty'] = db[eci_1.get()]['mass']
            new_mole_qty = eci_1_qty.get()/dbr['R1']['eci_1_qty']
            e_eci_1_M_qty.delete(0, tk.END)
            e_eci_1_M_qty.insert(0, new_mole_qty)
            print('e_eci_1_M_qty ', e_eci_1_M_qty)
            print('type e_eci_1_M_qty is', type(e_eci_1_M_qty))
        elif item == "M_qty":
            dbr['R1']['eci_1_qty'] = db[eci_1.get()]['mass']
            current_eci_1_qty = dbr['R1']['eci_1_qty']
            #print('current_eci_1_qty ', current_eci_1_qty)
            #type(current_eci_1_qty)
            new_eci_1_qty = eci_1_M_qty.get() * current_eci_1_qty
            dbr['R1']['eci_1_qty'] = new_eci_1_qty
            e_eci_1_qty.delete(0, tk.END)
            e_eci_1_qty.insert(0, new_eci_1_qty)
        elif item == "T_qty":
            print("1997 Element is ", dbr['R1']['eci_1_formula'], ". Item is ", item)
        elif item == "T_units":
            ''' Units are changed via a combobox selection. '''
            print("2000 Element is ", dbr['R1']['eci_1_formula'], ". Item is ", item)
        elif item == "P_qty":
            print("2002 Element is ", dbr['R1']['eci_1_formula'], ". Item is ", item)
        elif item == "P_units":
            ''' Units are changed via a combobox selection. '''
            print("2005 Element is ", dbr['R1']['eci_1_formula'], ". Item is ", item)
        #else: print("Element is ", dbr['R1']['eci_1_formula'], ". Item is ", item)
    elif dbr['R1']['eci_1_units'] == 'liters(g)':
        print("2025 dbr['R1']['eci_1_units'] = ", dbr['R1']['eci_1_units'])
        pvnrt(eci, item)

#pdb.set_trace()
def pvnrt(eci, item):
    print('1986 In process pvnrt ', eci, item)
    ''' Calculate volume given pressure, R constant, and temperature. pv = nRt'''
    R = 0.082057 # R value for these units
    if eci == eci_1.get():
        print('In pvnrt if eci == eci_1:')
        V = float(eci_1_qty.get())
        n = float(eci_1_M_qty.get())
        if eci_1_temp_units.get() == 'C':
            T = 273.15 + float(e_Temp_Qty_1.get())  #C_to_K(float(e_Temp_Qty_1.get())) got TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'
            dbr['R1']['eci_1_temp_calc_qty'] = T
        elif eci_1_temp_units.get() == 'K':
            T = float(e_Temp_Qty_1.get())
            dbr['R1']['eci_1_temp_calc_qty'] = T
        elif eci_1_temp_units.get() == 'F':
            T = (5/9) * float(e_Temp_Qty_1.get()) + 32 + 273.15
            dbr['R1']['eci_1_temp_calc_qty'] = T
        if eci_1_press_units.get() == 'atm':
            P = float(e_Press_Qty_1.get())
            dbr['R1']['eci_1_press_display_qty'] = P
        elif eci_1_press_units.get() == 'torr' or eci_1_press_units.get() == 'mmHg':
            P = float(e_Temp_Qty_1.get()) * 760
            dbr['R1']['eci_1_press_display_qty'] = P
        print('2008 n = ', n,'T = ', T,'P = ', P, 'V = ',V)
        if item == 'M_qty':
            print("2010 in if item == 'M_qty':")
            n = float(eci_1_M_qty.get())    # getdouble
            try:
                V = n*R*T/P
                e_eci_1_qty.delete(0, 'end')
                e_eci_1_qty.insert(0, V)
                print(n, T, P, V)
            except: print('Error in vol = n*R*T/P item == M_qty')
        elif item == 'qty':
            print("2019 in if item == 'qty':")
            V = float(eci_1_qty.get())
            try:
                n = (P*V)/(R*T)
                e_eci_1_M_qty.delete(0, tk.END)
                e_eci_1_M_qty.insert(0, n)
                print('2025 n is ', n, ' V is  ', V)
            except: print('Error in vol = n*R*T/P item == qty')
    elif eci == eci_2.get():
        V = float(eci_2_qty.get())
        n = float(eci_2_M_qty.get())
        if eci_2_temp_units.get() == 'C':
            T = 273.15 + float(e_Temp_Qty_2.get())  #C_to_K(float(e_Temp_Qty_1.get())) got TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'
            dbr['R1']['eci_2_temp_calc_qty'] = T
        elif eci_2_temp_units.get() == 'K':
            T = float(e_Temp_Qty_2.get())
            dbr['R1']['eci_2_temp_calc_qty'] = T
        elif eci_2_temp_units.get() == 'F':
            T = (5/9) * float(e_Temp_Qty_2.get()) + 32 + 273.15
            dbr['R1']['eci_2_temp_calc_qty'] = T
        if eci_2_press_units.get() == 'atm':
            P = float(e_Press_Qty_2.get())
            dbr['R1']['eci_2_press_display_qty'] = P
        elif eci_2_press_units.get() == 'torr' or eci_2_press_units.get() == 'mmHg':
            P = float(e_Temp_Qty_2.get()) * 760
            dbr['R1']['eci_2_press_display_qty'] = P
        print('2045 n = ', n,'T = ', T,'P = ', P, 'V = ',V)
        if item == 'M_qty':
            print("2047 in if item == 'M_qty':")
            n = float(eci_2_M_qty.get())    # getdouble
            try:
                V = n*R*T/P
                e_eci_2_qty.delete(0, 'end')
                e_eci_2_qty.insert(0, V)
                print(n, T, P, V)
            except: print('Error in vol = n*R*T/P item == M_qty')
        elif item == 'qty':
            print("2056 in if item == 'qty':")
            V = float(eci_2_qty.get())
            try:
                n = (P*V)/(R*T)
                e_eci_2_M_qty.delete(0, tk.END)
                e_eci_2_M_qty.insert(0, n)
                print('2026 n is ', n, ' V is  ', V)
            except: print('Error in vol = n*R*T/P item == qty')
    elif eci == eci_3.get():
        V = float(eci_3_qty.get())
        n = float(eci_3_M_qty.get())

    #temp = 0.0


def eci_1_qty_adjusted(value):
    print('2072 eci_1_qty_adjusted event procedure called.')
    mole_mass_change(dbr['R1']['eci_1_formula'], 'qty')

def eci_1_M_qty_adjusted(value):
    print('2076 eci_1_qty_adjusted event procedure called.')
    mole_mass_change(dbr['R1']['eci_1_formula'], 'M_qty')

def eci_1_Temp_qty_adjusted(value):
    print('2080 eci_1_qty_adjusted event procedure called.')
    mole_mass_change(dbr['R1']['eci_1_formula'], 'T_qty')

def eci_1_Temp_units_adjusted(value):
    print('2084 eci_1_qty_adjusted event procedure called.')
    mole_mass_change(dbr['R1']['eci_1_formula'], 'T_units')

def eci_1_Press_qty_adjusted(value):
    mole_mass_change(dbr['R1']['eci_1_formula'], 'P_qty')
    print('2089 eci_1_Press_qty_adjusted event procedure called.')

def eci_1_Press_units_adjusted(value):
    print('2092 eci_1_Press_units_adjusted event procedure called.')
    mole_mass_change(dbr['R1']['eci_1_formula'], 'P_units')

def eci_2_qty_adjusted(value):
    print('2096 eci_2_qty_adjusted event procedure called.')
    mole_mass_change(dbr['R1']['eci_2_formula'], 'qty')

def eci_2_M_qty_adjusted(value):
    print('2100 eci_2_qty_adjusted event procedure called.')
    mole_mass_change(dbr['R1']['eci_2_formula'], 'M_qty')

def eci_2_Temp_qty_adjusted(value):
    print('2104 eci_2_qty_adjusted event procedure called.')
    mole_mass_change(dbr['R1']['eci_2_formula'], 'T_qty')

def eci_2_Temp_units_adjusted(value):
    print('2108 eci_2_qty_adjusted event procedure called.')
    mole_mass_change(dbr['R1']['eci_2_formula'], 'T_units')

def eci_2_Press_qty_adjusted(value):
    mole_mass_change(dbr['R1']['eci_2_formula'], 'P_qty')
    print('2113 eci_2_Press_qty_adjusted event procedure called.')

def eci_2_Press_units_adjusted(value):
    print('2116 eci_2_Press_units_adjusted event procedure called.')
    mole_mass_change(dbr['R1']['eci_2_formula'], 'P_units')

def xeci_2_qty_adjusted(value):
    print('2001 eci_2_qty_adjusted event procedure called.', value)
    print('e_eci_2_qty is ', e_eci_2_qty.get())
    current_eci_2_units = dbr['R1']['eci_2_units']
    print('current_eci_2_units is ', current_eci_2_units)
    if dbr['R1']['eci_2_units'] == 'grams':
        ''' I can't just adjust the eci_1_qty, I need to determine what it should be based on units.
        Since units are in grams, I need to retrieve the element atomic mass and use it for calculations.'''
        print("1750 dbr['R1']['eci_2_units'] == ", dbr['R1']['eci_2_units'])
        dbr['R1']['eci_2_qty'] = db[eci_2.get()]['mass']
        new_mole_qty = eci_2_qty.get()/dbr['R1']['eci_2_qty']
        e_eci_2_M_qty.delete(0, tk.END)
        e_eci_2_M_qty.insert(0, new_mole_qty)

def xeci_2_M_qty_adjusted(value):
    print('eci_2_M_qty_adjusted event procedure called.', value)
    print('eci_2_M_qty is ', eci_2_M_qty.get())
    current_eci_2_units = dbr['R1']['eci_2_units']
    print('current_eci_2_units is ', current_eci_2_units)
    if dbr['R1']['eci_2_units'] == 'grams':
        print("1750 dbr['R1']['eci_2_units'] == ", dbr['R1']['eci_2_units'])
        ''' Reset the record quantity to the element atomic mass before doing calculations. '''
        dbr['R1']['eci_2_qty'] = db[eci_2.get()]['mass']
        ''' current_eci_2_qty may be mass in grams or some other quantity of the current units.'''
        current_eci_2_qty = dbr['R1']['eci_2_qty']
        print('current_eci_2_qty is ', current_eci_2_qty)
        new_eci_2_qty = eci_2_M_qty.get() * current_eci_2_qty
        e_eci_2_qty.delete(0, tk.END)
        e_eci_2_qty.insert(0, new_eci_2_qty)

def eci_3_qty_adjusted(value):
    print('eci_3_qty_adjusted event procedure called.', value)
    print('e_eci_3_qty is ', e_eci_3_qty.get())
    current_eci_3_units = dbr['R1']['eci_3_units']
    print('current_eci_3_units is ', current_eci_3_units)
    if dbr['R1']['eci_3_units'] == 'grams':
        ''' I can't just adjust the eci_1_qty, I need to determine what it should be based on units.
        Since units are in grams, I need to retrieve the element atomic mass and use it for calculations.'''
        print("dbr['R1']['eci_3_units'] == ", dbr['R1']['eci_3_units'])
        dbr['R1']['eci_3_qty'] = db[eci_3.get()]['mass']
        new_mole_qty = eci_3_qty.get()/dbr['R1']['eci_3_qty']
        e_eci_3_M_qty.delete(0, tk.END)
        e_eci_3_M_qty.insert(0, new_mole_qty)

def eci_3_M_qty_adjusted(value):
    current_eci_3_units = dbr['R1']['eci_3_units']
    print('current_eci_3_units is ', current_eci_3_units)
    if dbr['R1']['eci_3_units'] == 'grams':
        print("dbr['R1']['eci_3_units'] == ", dbr['R1']['eci_3_units'])
        ''' Reset the record quantity to the element atomic mass before doing calculations. '''
        dbr['R1']['eci_3_qty'] = db[eci_3.get()]['mass']
        ''' current_eci_3_qty may be mass in grams or some other quantity of the current units.'''
        current_eci_3_qty = dbr['R1']['eci_3_qty']
        print('current_eci_3_qty is ', current_eci_3_qty)
        new_eci_3_qty = eci_3_M_qty.get() * current_eci_3_qty
        e_eci_3_qty.delete(0, tk.END)
        e_eci_3_qty.insert(0, new_eci_3_qty)

def Fill_Product_Comboboxes():
    print('2059 Entered Fill_Product_Comboboxes')
    cb_4_type = "compounds"
    cb_Select_CB4.set(cb_4_type)
    cnd_set = set(compounds_names_dict.values())
    '''{'C5H12', 'HNO3', 'KOH', 'N2O5', 'Al4C3','SO3', 'Na2SO4', 'C6H8O7',
     'NH3', 'C9H20', 'HBr', 'HCl', 'HNO2', 'KBr', 'LiCl', 'C3H8', 'C6H14', 
     'HF', 'C8H18', 'CO', 'HC2H3O2', 'H2SO3', 'C18H38', 'CaI', 'CO2', 'H3PO4', 
     'CaH2PO4', 'N2H4', 'N2O', 'C7H16', 'CaOH2', 'AlCl3', 'C4H10', 'NO', 'H2SO4', 
     'Ca3P2', 'C2H6', 'HCN', 'Mg3N2', 'NaCl', 'NaOH', 'HI', 'CdS', 'NaHCO3', 
     'CH4', 'BCl3', 'C4H10_M', 'C10H22', 'Na2O', 'CsF', 'HClO4', 'H2S', 'NO2', 
     'N2O4', 'H2CO3', 'Ar2He2Kr2Ne2Xe2Rn2', 'C14H30', 'PF5', 'SO2', 'IF7'}'''
    # iterate throught cnd_set items dictionary above
    # if the alpha_list == the compound dictionary elements string
    # AlCl3 = dict(formula= 'AlCl3', elements= 'AlCl',name= 'aluminum_chloride')
    # Thus, if the set item is AlCl3, and the alpha_list is AlCl
    # When the loop gets to AlCl3, alpha_list = AlCl will equal AlCl3(elements) = AlCl
    # if the above conditions are satisfied, create two new strings:
    # one to set the values of cb_4 formula values and one to set the cd_4 names values.
    #for c in cnd_set:
    #    print(c, c.elements)
    print(cnd_set)
    print("cb_4_type is ", cb_Select_CB4.get())
    print('Exited Fill_Product_Comboboxes')

def Oxidation_Reduction():
    """This function has been entered after elements have been selected and the Continue button pressed."""
    e_Explanation.insert(END, "Oxidation_Reduction process entered\n")
    print('2086 Entering Oxidation_Reduction() ')
    Oxidation_Rate()
    cb_1_type = cb_Select_CB1.get()  # Get the selected type of: element, compound, or ion
    print('eci_1_type = ', cb_1_type)
    eci_1 = cb_eci_1.get()
    print('eci_1 = ', eci_1)
    if cb_1_type == 'elements':
        '''  *** The following works! '''

        # eci_db['eci_1']['name']
        eci_d['eci_1']['name'] = db[eci_1]['name']
        # eci_db[eci_1]['name'] = db[eci_1]['name']
        print("eci_db['eci_1']['name'] is ", eci_d['eci_1']['name'])
        eci_1_name = db[eci_1]['name']
        print("eci_1_name is ", eci_1_name)   #db[eci_1]['name']
        print("db[eci_1]['name'] is ", db[eci_1]['name'])
        eci_1_col = db[eci_1]['column']
        eci_1_mass = db[eci_1]['mass']
        eci_1_valence = db[eci_1]['valence']
        eci_d['eci_1']['column'] = db[eci_1]['column']
        eci_d['eci_1']['mass'] = db[eci_1]['mass']
        eci_d['eci_1']['valence'] = db[eci_1]['valence']
        print("eci_db['eci_1']['column'] is ", eci_d['eci_1']['column'])
        print("eci_db['eci_1']['mass'] is ", eci_d['eci_1']['mass'])
        print("eci_db['eci_1']['valence'] is ", eci_d['eci_1']['valence'])
        # print("db[eci_1]['name'] is ", eci_1_name)
        # print("db[eci_1]['column'] is ", eci_1_col)
        # print("db[eci_1]['mass'] is ", eci_1_mass)
        # print("db[eci_1]['valence'] is ", eci_1_valence)
        # print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
    elif cb_1_type == 'compounds':
        # eci_1 = cb_eci_1.get()
        # print('eci_1 = ', eci_1)
        e_Explanation.insert(END, "Oxidation_Reduction process entered\n")
        print("Oxidation_Reduction eci_1 can't process compounds yet")
    elif cb_1_type == 'ions':
        # eci_1 = cb_eci_1.get()
        # print('eci_1 = ', eci_1)
        e_Explanation.insert(END, "Error in Oxidation_Reduction eci_1 can't process compounds yet")
    else:
        print("Oxidation_Reduction process eci_1 else clause")
    cb_2_type = cb_Select_CB2.get()  # Get the selected type of: element, compound, or ion
    print('eci_2_type = ', cb_2_type)
    if cb_2_type == 'elements':
        eci_2 = cb_eci_2.get()
        print('eci_2 = ', eci_2)
        '''  *** The following works! '''
        eci_2_name = db[eci_2]['name']
        eci_2_col = db[eci_2]['column']
        eci_2_mass = db[eci_2]['mass']
        eci_2_valence = db[eci_2]['valence']
        print("db[eci_2]['name'] is ", eci_2_name)
        print("db[eci_2]['column'] is ", eci_2_col)
        print("db[eci_2]['mass'] is ", eci_2_mass)
        print("db[eci_2]['valence'] is ", eci_2_valence)
        # print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
    elif cb_2_type == 'compounds':
        # eci_2 = cb_eci_2.get()
        # print('eci_2 = ', eci_2)
        print("Error in Oxidation_Reduction eci_2 can't process compounds yet")
    elif cb_2_type == 'ions':
        # eci_2 = cb_eci_2.get()
        # print('eci_2 = ', eci_2)
        print("Error in Oxidation_Reduction eci_2 can't process ions yet")
    else:
        print("Error in Oxidation_Reduction process eci_2 else clause")
    cb_3_type = cb_Select_CB3.get()  # Get the selected type of: element, compound, or ion
    print('eci_3_type = ', cb_3_type)
    eci_3 = cb_eci_3.get()
    print('eci_3 = ', eci_3)
    if cb_3_type == 'elements':
        # eci_3 = cb_eci_3.get()
        # print('eci_3 = ', eci_3)
        '''  *** The following works! '''
        eci_3_name = db[eci_3]['name']
        eci_3_col = db[eci_3]['column']
        eci_3_mass = db[eci_3]['mass']
        eci_3_valence = db[eci_3]['valence']
        print("db[eci_3]['name'] is ", eci_3_name)
        print("db[eci_3]['column'] is ", eci_3_col)
        print("db[eci_3]['mass'] is ", eci_3_mass)
        print("db[eci_3]['valence'] is ", eci_3_valence)
        # print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
    elif cb_3_type == 'compounds':
        # eci_3 = cb_eci_3.get()
        # print('eci_3 = ', eci_3)
        print("Error in Oxidation_Reduction eci_3 can't process compounds yet")
    elif cb_3_type == 'ions':
        # eci_3 = cb_eci_3.get()
        # print('eci_3 = ', eci_3)
        print("Error in Oxidation_Reduction eci_3 can't process ions yet")
    elif cb_3_type == "":
        pass
    else:
        e_Explanation.insert(END, "Error in Oxidation_Reduction process eci_3 else clause\n")

    # if cb_eci_1.get() == 'elements':
    #    eci_1 = cb_eci_1.get()
    #    print('eci_1 = ', eci_1)
    #    print('eci_1_type = ', cb_eci_1.get())


def Precipitation():
    print('2189 Entered Precipitation')
    """ print("Pressed update_record button") """
    e_Explanation.insert(END, "Precipitation process entered\n")
    # print("Precipitation process entered")


def Oxidation_Rate():   #Based on eci type, call appropriate Oxidation_Rate function
    print('2196 Entering Oxidation_Rate() ')

    cb_1_type = cb_Select_CB1.get()
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()
    if cb_1_type == 'elements' and cb_2_type == 'elements' and cb_3_type == 'elements' or cb_3_type == "":
        Oxidation_Rate_Elements()
    elif cb_1_type == 'compounds' or cb_2_type == 'compounds' and cb_3_type == 'compounds':
        Oxidation_Rate_Compounds()
    elif cb_1_type == 'ions' or cb_2_type == 'ions' and cb_3_type == 'ions':
        Oxidation_Rate_Ions()
    else:
        e_Explanation.insert(END, "Oxidation_Rate process fell through to else clause\n")


''' Oxidation_Rate_Compounds and Oxidation_Rate_Ions are placeholders for future use as needed. '''


def Oxidation_Rate_Compounds():
    e_Explanation.insert(END, "Entered Oxidation_Rate_Compounds process\n")


def Oxidation_Rate_Ions():
    e_Explanation.insert(END, "Entered Oxidation_Rate_Ions process\n")

def set_eci_d_balance_variables():
    ''' The following demonstrate the direct assignments of frame values
    from the element dictionary. '''
    print('In set_eci_d_balance_variables()')

    eci_d['eci_1']['eci'] = cb_eci_1.get()
    eci_d['eci_2']['eci'] = cb_eci_2.get()
    eci_d['eci_3']['eci'] = cb_eci_3.get()
    print("eci_d['eci_1']['eci'] is ", eci_d['eci_1']['eci'])
    print("eci_d['eci_2']['eci'] is ", eci_d['eci_2']['eci'])
    print("eci_d['eci_3']['eci'] is ", eci_d['eci_3']['eci'])
    eci_d['eci_1']['eci_type'] = cb_Select_CB1.get()
    eci_d['eci_2']['eci_type'] = cb_Select_CB2.get()
    eci_d['eci_3']['eci_type'] = cb_Select_CB3.get()
    print("eci_d['eci_1']['eci_type'] is ", eci_d['eci_1']['eci_type'])
    print("eci_d['eci_2']['eci_type'] is ", eci_d['eci_2']['eci_type'])
    print("eci_d['eci_3']['eci_type'] is ", eci_d['eci_3']['eci_type'])

def Oxidation_Rate_Elements():
    ''' This function has been entered after elements have been selected and the Continue button pressed. Each item is an element. Compounds and ions use a different function.
    It is necessary to get the valence and electronegativity values because the valence of some
    elements is determined by the relative electronegativity of the other elements.'''
    cb_eci_1_units.set('grams')
    cb_eci_2_units.set('grams')
    cb_eci_4_units.set('grams')

    e_Explanation.insert(END, "Oxidation_Rate_Elements process entered\n")
    print(' Entering Oxidation_Rate_Elements() ')

    ''' The following has already been done in the Oxidation_Rate() function
    cb_1_type = cb_Select_CB1.get()
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()
    '''
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    eci_3 = cb_eci_3.get()
    ''' Set the values in the eci frame dictionary. '''
    # eci_1_temp_units = cb_1_Temp_Units.get() # Move to after balance process
    set_eci_d_balance_variables()

    ''' if eci_db['eci_1']['eci_type'] == 'elements': is no longer needed
    because all non-elements have been moved to another function. '''
    ''' These lines get values of the element from the element dictionary. '''
    eci_1_name = db[eci_1]['name']
    eci_1_mass = db[eci_1]['mass']
    eci_1_group = db[eci_1]['_group']
    eci_1_valence = db[eci_1]['valence']
    eci_1_electronegativity = db[eci_1]['electronegativity']
    eci_1_qty = eci_1_mass
    print('e_eci_1_qty is at line 1638', eci_1_qty)
    print("db[eci_1]['name'] is ", eci_1_name)
    print("db[eci_1]['mass'] is ", eci_1_mass)
    print("db[eci_1]['_group'] is ", eci_1_group)
    print("db[eci_1]['valence'] is ", eci_1_valence)
    print("db[eci_1]['electronegativity'] is ", eci_1_electronegativity)
    ''' if eci_db['eci_2']['eci_type'] == 'elements':  in no longer needed. '''
    eci_2_name = db[eci_2]['name']
    eci_2_mass = db[eci_2]['mass']
    eci_2_group = db[eci_2]['_group']
    eci_2_valence = db[eci_2]['valence']
    eci_2_electronegativity = db[eci_2]['electronegativity']
    print("db[eci_2]['name'] is ", eci_2_name)
    print("db[eci_2]['_group'] is ", eci_2_group)
    print("db[eci_2]['valence'] is ", eci_2_valence)
    print("db[eci_2]['electronegativity'] is ", eci_2_electronegativity)
    if eci_d['eci_3']['eci_type'] == 'elements':
        eci_3_name = db[eci_3]['name']
        eci_3_group = db[eci_3]['_group']
        eci_3_valence = db[eci_3]['valence']
        eci_3_electronegativity = db[eci_3]['electronegativity']
        print("db[eci_3]['name'] is ", eci_3_name)
        print("db[eci_3]['_group'] is ", eci_3_group)
        print("db[eci_3]['valence'] is ", eci_3_valence)
        print("db[eci_3]['electronegativity'] is ", eci_3_electronegativity)
        print("In Oxidation_Rate_Elements. Function does not yet work for 3 elements.")
    if eci_1_valence.isnumeric():
        ''' This process only works for metals that have single valence values. '''
        ''' Set the dictionary values. Valence may have multiple values. In these cases, it has only one value.
        Oxidation_State only has one value that is set for this case. '''
        eci_1_Oxidation_State = eci_1_valence
        db[eci_1]['valence'] = eci_1_valence
        db[eci_1]['Oxidation_State'] = eci_1_valence
        print("eci_1_Oxidation_State is ", eci_1_Oxidation_State)
        print("db[eci_1]['valence'] is numeric ", eci_1_valence)
        ''' eci_db['eci_2']['eci_type'] == 'elements': '''
        if eci_2_valence.isnumeric():
            eci_2_Oxidation_State = eci_2_valence
            db[eci_2]['valence'] = eci_2_valence
            db[eci_2]['Oxidation_State'] = eci_2_Oxidation_State
            print("db[eci_2]['valence'] is numeric ", eci_2_valence)
            print("eci_1_Oxidation_State is ", eci_1_Oxidation_State)
            ''' Now we can solve for the valences'''
        elif not eci_2_valence.isnumeric():
            print("In elif not eci_2_valence.isnumeric")
            if eci_2_group == "7A":
                print("db[eci_2]['_group'] is ", eci_2_group)
                if eci_1_electronegativity < eci_2_electronegativity:
                    eci_2_valence = -1
                    eci_2_Oxidation_State = eci_2_valence
                    db[eci_2]['Oxidation_State'] = eci_2_Oxidation_State
                    print("eci_2_Oxidation_State is ", eci_2_Oxidation_State)
                    ''' The following can be moved to synthesis. '''
                    eci_1_M_qty = 1
                    e_eci_1_qty = eci_1_mass # e_eci_1_qty = eci_1_mass
                    print('e_eci_1_qty is at line 1693', e_eci_1_qty)
                    #e_eci_1_qty.delete(0)
                    #e_eci_1_qty.insert(0, eci_1_mass)
                    #print('e_eci_1_qty is at line 1696', e_eci_1_qty)
                    e_eci_1_M_qty.delete(0)
                    e_eci_1_M_qty.insert(0, eci_1_M_qty)
                    eci_2_M_qty = eci_1_valence  # This is correct. Cross assign valences to quantities
                    e_eci_2_M_qty.delete(0, END)
                    e_eci_2_M_qty.insert(0, eci_2_M_qty)
                    ''' Set the type and value of the compound.'''
                    ''' These functions will be moved to other processes when they are defined.
                    Oxidation_Rate_Elements will only store the oxidation states in the frame directories. '''
                    cb_4_type = "compound"
                    eci_4_type = "compound"
                    ''' Set a temporary variable to hold the formula variable
                    because the formula assumes quantity is 1, so it doen't need to be shown'''
                    eci_1a = eci_1
                    eci_2a = eci_2
                    if eci_2_valence == -1:
                        eci_1a = eci_1
                    elif not eci_2_valence == -1:
                        eci_1a = eci_1 + str(eci_2_valence)
                    if eci_1_valence == '1':
                        eci_2a = eci_2
                        print('eci_2a is ', eci_2a)
                    elif not eci_1_valence == '1':
                        eci_2a = eci_2 + str(eci_1_valence)
                    eci_4 = eci_1a + eci_2a
                    ''' Need to set cb_eci_4 selected item to eci_4'''
                    cb_eci_4.set(eci_4)
                    e_eci_4_M_qty.delete(0, END)
                    e_eci_4_M_qty.insert(0, 1)
                    print("eci_4 is ", eci_4)
                    print("e_eci_1_M_qty is ", e_eci_1_M_qty.get())
                    print("e_eci_2_M_qty is ", e_eci_2_M_qty.get())
                elif eci_1_electronegativity > eci_2_electronegativity:
                    print(
                        "In Oxidation_Rate_Elements eci_2 group 7A -- eci_1_electronegativity > eci_2_electronegativity")
            elif eci_2_group == "6A":  # Will need to exclude Oxygen for some compounds
                print("In Oxidation_Rate_Elements eci_2_group == 6A.")
                db[eci_2]['_group'] = eci_2_group
                print("db[eci_2]['_group'] is ", eci_2_group)
                if eci_1_electronegativity < eci_2_electronegativity:
                    eci_2_valence = -2
                    eci_1_M_qty = -eci_2_valence
                    eci_2_M_qty = eci_1_valence
                    eci_2_Oxidation_State = eci_2_valence
                    print("eci_2_Oxidation_State is ", eci_2_Oxidation_State)
                    if eci_2_valence == -2 and eci_1_valence == "1":
                        print("if eci_2_valence == -2 and eci_1_valence == 1:")
                        print("eci_1 is", eci_1, "eci_2_valence is", eci_2_valence, "eci_2 is", eci_2)
                        eci_4 = eci_1 + str(abs(eci_2_valence)) + eci_2
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, eci_1_M_qty)
                        eci_2_M_qty = eci_1_valence  # This is correct. Cross assign valences to quantities
                        e_eci_2_M_qty.delete(0, END)
                        e_eci_2_M_qty.insert(0, eci_2_M_qty)
                    elif -int(eci_2_valence) == int(eci_1_valence):
                        print("-eci_2_valence is", -eci_2_valence)
                        eci_4 = eci_1 + eci_2
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, 1)
                        e_eci_2_M_qty.delete(0, END)
                        e_eci_2_M_qty.insert(0, 1)
                    elif not -int(eci_2_valence) == int(eci_1_valence):
                        eci_4 = eci_1 + str(-eci_2_valence) + eci_2 + str(eci_1_valence)
                        print("-int(eci_2_valence) is", -int(eci_2_valence))
                        print("int(eci_1_valence) is", int(eci_1_valence))
                        # eci_4 = eci_1 + eci_2 + eci_1_valence
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, eci_1_M_qty)
                        eci_2_M_qty = eci_1_valence  # This is correct. Cross assign valences to quantities
                        e_eci_2_M_qty.delete(0, END)
                        e_eci_2_M_qty.insert(0, eci_2_M_qty)
                    cb_eci_4.set(eci_4)
                    e_eci_4_M_qty.delete(0, END)
                    e_eci_4_M_qty.insert(0, 1)
                    print("eci_4 is ", eci_4)
                    eci_1_massa = float(eci_1_M_qty) * float(eci_1_mass)
                    print("eci_1_massa is ", eci_1_massa)
                    e_eci_1_qty.delete(0)
                    e_eci_1_qty.insert(0, eci_1_massa)
                    print('e_eci_1_qty is at line 1772', e_eci_1_qty)
                    e_eci_2_qty.delete(0)
                    e_eci_2_qty.insert(0, float(eci_2_M_qty) * float(eci_2_mass))
                    # eci_1_M_qty = 1

            elif not eci_2_group == "6A" and not eci_2_group == "7A":
                print("In Oxidation_Rate_Elements not eci_2_group == 6A or 7A.")
            elif eci_1_electronegativity > eci_1_electronegativity:
                pass
    elif not eci_1_valence.isnumeric():  # if eci_1_valence is a string of valence values
        print("In Oxidation_Rate_Elements not eci_1_valence.isnumeri.")
    else:
        e_Explanation.insert(END, "In Oxidation_Rate process else clause\n")

def Acid_Base():
    e_Explanation.insert(END, "Acid_Base process entered\n")

def Combustion():
    e_Explanation.insert(END, "Combustion process entered\n")

def Decomposition():
    e_Explanation.insert(END, "Decomposition process entered\n")

def Neutralization():
    e_Explanation.insert(END, "Neutralization process entered\n")


def Decompostion():
    e_Explanation.insert(END, "Decompostion process entered\n")

def Precipitation():
    e_Explanation.insert(END, "Precipitation process entered\n")

def Refinement():
    e_Explanation.insert(END, "Refinement process entered\n")

def Single_Replacement():
    e_Explanation.insert(END, "Single_Replacement process entered\n")

def Double_Replacement():
    e_Explanation.insert(END, "Double_Replacement process entered\n")

def Metathesis():
    e_Explanation.insert(END, "Metathesis process entered\n")


def Oxidization():
    e_Explanation.insert(END, "Oxidization process entered\n")

def Synthesis():
    '''
    Option 1. The user will select a product and the program will determine the reactants
    and the by-products.
    Option 2. The user will start by entering compounds and or elements in the left side of the
    GUI. Since there are so many possibilities, the user will need to specify the reactants and
    the primary product. Any other products will be considered by-products.
    Start by counting the number of reactants, alphabetize them, look up all the products
    that have any combination of those reactant elements, and fill the product combobox
    with that list. Since the program will not know which items will be products and which
    will be by-products, the list must contain all the compounds that have any of the reactants.
    All products that do not have those elements can be eliminated from the products comboboxes --
    even catalysts can be eliminated because they will be specified in a separate combobox.
    When a primary product has been selected, start the synthesis process by calculating the
    oxidation status, then

    '''
    e_Explanation.insert(END, "Synthesis process entered\n")
    print("2479 Synthesis process entered")
    CountElements()
    AlphabetizeElements()
    Fill_Product_Comboboxes()
    Oxidation_Rate()

    ''' Consider starting with a compound formula or name.'''

    cb_1_type = cb_Select_CB1.get()  # Get the selected type of: element, compound, or ion
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()

    print("cb_1_type is", cb_1_type, "cb_2_type is", cb_2_type)

    # e_Explanation.insert(tk.END, "cb_1_type = cb_Select_CB1.get() step\n")

    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    # if cb_1_type == 'elements':
    #    eci_1_valence = db[eci_1]['valence']
    #    eci_2_valence = db[eci_2]['valence']
    #    print("eci_1 is", eci_1, "eci_2 is", eci_2)
    # eci_3 = cb_eci_3.get()
    # and eci_1 != ''
    # eci_1_valence = db[eci_1]['valence']
    # eci_3_group = db[eci_3]['_group']
    '''
    Cut out code that determines oxidation rate for elements.
    '''
    if cb_1_type == 'compounds':
        eci_1 = cb_eci_1.get()
        print('eci_1 is ', eci_1)
        eci_1_name = c_db[eci_1]['name']
        # eci_1_name = c_db[eci_1]['name']
        print('eci_1 is ', eci_1)
        # e_Explanation.insert(tk.END, "In Synthesis, compounds.\n")

def set_eci_db_eci_1_qty(qty):
    set_eci_db_eci_1_qty = qty
    print('2517 set_eci_db_eci_1_qty is ', set_eci_db_eci_1_qty)


''' function may not be needed
def eci_1_qty_changed(eventObject):    #callback
    eci_1_qty = e_eci_1_qty.get()   #e_eci_1_qty
    print('eci_1_qty is ', eci_1_qty)'''


def callback_set_temp_units(eventObject):
    pass
    ''' Whenever a temperature units combo box is selected, update the eci_db variable. '''
    '''
    eci_1_temp_units = cb_1_Temp_Units.get()
    eci_2_temp_units = cb_2_Temp_Units.get()
    eci_3_temp_units = cb_3_Temp_Units.get()
    eci_4_temp_units = cb_4_Temp_Units.get()
    eci_5_temp_units = cb_5_Temp_Units.get()
    eci_6_temp_units = cb_6_Temp_Units.get()
    eci_d['eci_1']['display_temp_units'] = cb_1_Temp_Units.get()
    eci_d['eci_2']['display_temp_units'] = cb_2_Temp_Units.get()
    eci_d['eci_3']['display_temp_units'] = cb_3_Temp_Units.get()
    eci_d['eci_4']['display_temp_units'] = cb_4_Temp_Units.get()
    eci_d['eci_5']['display_temp_units'] = cb_5_Temp_Units.get()
    eci_d['eci_6']['display_temp_units'] = cb_6_Temp_Units.get()
    '''

def callback_set_press_units(eventObject):
    ''' Whenever a temperature units combo box is selected, update the eci_db variable. '''
    '''
    eci_1_press_units = cb_1_Press_Units.get()
    eci_2_press_units = cb_2_Press_Units.get()
    eci_3_press_units = cb_3_Press_Units.get()
    eci_4_press_units = cb_4_Press_Units.get()
    eci_5_press_units = cb_5_Press_Units.get()
    eci_6_press_units = cb_6_Press_Units.get()
    eci_d['eci_1']['display_press_units'] = cb_1_Press_Units.get()
    eci_d['eci_2']['display_press_units'] = cb_2_Press_Units.get()
    eci_d['eci_3']['display_press_units'] = cb_3_Press_Units.get()
    eci_d['eci_4']['display_press_units'] = cb_4_Press_Units.get()
    eci_d['eci_5']['display_press_units'] = cb_5_Press_Units.get()
    eci_d['eci_6']['display_press_units'] = cb_6_Press_Units.get()
    '''

def Reset_Product_Boxes():
    cb_eci_2.set("")
    cb_eci_2_N.set("")
    e_eci_2_M_qty.delete(0, END)
    cb_eci_3.set("")
    cb_eci_3_N.set("")
    e_eci_3_M_qty.delete(0, END)
    #cb_eci_4.set("")
    #cb_eci_4_N.set("")
    #e_eci_4_M_qty.delete(0, END)
    cb_eci_5.set("")
    cb_eci_5_N.set("")
    e_eci_5_M_qty.delete(0, END)
    cb_eci_6.set("")
    cb_eci_6_N.set("")
    e_eci_6_M_qty.delete(0, END)

def Parse_Reactants():  # 'He2SO4'
    ''' I need to parse for number, uppercase, and lowercase. Leading number always applies to an element or formula,
    later numbers are assumed to apply to the preceeding element.
    '''
    e_Explanation.insert(END, "Parse_Reactants process entered\n")
    if cb_Select_CB1.get() == 'compounds':
        eci_1 = cb_eci_1.get()
        compound = cb_eci_1.get()
        print('Parse_Reactants compound is ', compound)

    elif not cb_Select_CB1.get() == 'compounds':
        print('In Parse_Reactants, but compound type is not a set')
        e_Explanation.insert(END, "Parse_Compounds process entered, but compound type is not a set\n")

    else: print("Parse_Reactants process entered", cb_eci_1.get())


    #print('Parse_Reactants compound is ', compound)
    ''' Start with a normal compound which does not start with an integer.'''
    # For example: compound = 'Na2SO4'
    if cb_Select_CB1.get() == '':
        e_Explanation.insert(END, "Parse_Reactants process entered, but compound is empty string. \n")
    elif compound[0].isdigit():
        ''' If the leading character is a number, apply it to the whole formula. '''
        compound_formula_qty = compound[0]
        ''' Reset the compound to the string after the intial digit. '''
        compound = compound[1:]
        print('Parse_Reactants compound first character is integer ', compound[0])
        ''' The first character is not a number. '''
    elif not compound[0].isdigit():
        print('Pass to Parse_Compound') #Parse_Compound_ECI_1
        parsed_compound = Parse_Compound(compound)
        Display_Parsed_Reactant(parsed_compound)
        # Parse_Compound_ECI_1()
    else:
        print('In else clause of Parse_Compounds')
    # print(' If the leading character is a number, '
    #      'need to add it to the result of Parse_Compounds_1(compound).')

def Parse_Products():  # 'He2SO4'
    ''' I need to parse for number, uppercase, and lowercase. Leading number always applies to an element or formula,
    later numbers are assumed to apply to the preceeding element.
    '''
    e_Explanation.insert(END, "Parse_Products process entered\n")
    if cb_Select_CB4.get() == 'compounds':
        eci_1 = cb_eci_4.get()
        compound = cb_eci_4.get()
        print('Parse_Products compound is ', compound)

    elif not cb_Select_CB4.get() == 'compounds':
        print('In Parse_Products, but compound type is not a set')
        e_Explanation.insert(END, "Parse_Compounds process entered, but compound type is not a set\n")

    else: print("Parse_Products process entered", cb_eci_4.get())

    ''' Start with a normal compound which does not start with an integer.'''
    if compound == "":
        e_Explanation.insert(END, "Parse_Products process entered, but compound is empty string. \n")
    elif compound[0].isdigit():
        ''' If the leading character is a number, apply it to the whole formula. '''
        compound_formula_qty = compound[0]
        ''' Reset the compound to the string after the intial digit. '''
        compound = compound[1:]
        print('Parse_Products compound first character is integer ', compound[0])
        ''' The first character is not a number. '''
    elif not compound[0].isdigit():
        print('Pass to Parse_Products') #Parse_Compound_ECI_1
        parsed_compound = Parse_Compound(compound)
        Display_Parsed_Product(parsed_compound)
        # Parse_Compound_ECI_1()
    else:
        print('In else clause of Parse_Compounds')
    # print(' If the leading character is a number, '
    #      'need to add it to the result of Parse_Compounds_1(compound).')

def Parse_Compound(compound):
    ''' Got a compound from eci_1. Parse it. '''
    print('In Parse_Compound(compound): compound = ', compound)
    len_compound = len(compound)
    current_compound = []
    # print('len_compound is ', len_compound)
    while len(compound) >= 3:
        # print('len(compound) is ', len_compound)
        if compound[0].isupper() and compound[1].islower() and compound[2].isdigit():  # and compound[3].isupper():
            print(
                'In compound[0].isupper() and compound[1].islower() and compound[2].isdigit()')  # Re,removed  and compound[3].isupper()
            current_element_multiplier = 1
            current_element = compound[:2]
            current_element_multiplier = int(compound[2:3])
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[3:]
            print('elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper(): compound = ',
                  compound)
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound is ', current_compound)
        elif compound[0].isupper() and compound[1].islower() and compound[2].isdigit():  # and compound[3].isdigit()
            print('In compound[0].isupper() and compound[1].islower() and compound[2].isdigit()')
            print("Don't know if there are any of these.")
        elif compound[0].isupper() and compound[1].isupper():
            print('In compound[0].isupper() and compound[1].isupper()')
            current_element_multiplier = 1
            current_element = compound[0]
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[1:]
            print('In elif compound[1].isupper() and len(compound) > 1: compound = ', compound)
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound is ', current_compound)
        elif compound[0].isupper() and compound[1].islower() and compound[2].isupper():
            print('In compound[0].isupper() and compound[1].islower() and compound[2].isupper()')
            current_element_multiplier = 1
            current_element = compound[:2]
            current_element_multiplier = 1
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[2:]
            len_compound = len(compound)
            print('elif compound[0].isupper() and compound[1].islower() and compound[2].isupper(): compound = ',
                  compound)
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound, and length are ', current_compound, len_compound)
        elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper():
            print('In compound[0].isupper() and compound[1].isdigit() and compound[2].isupper()')
            current_element_multiplier = 1
            current_element = compound[:1]
            current_element_multiplier = int(compound[1:2])
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[2:]
            print('elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper(): compound = ',
                  compound)
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound is ', current_compound)
        elif compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit():
            print('In compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit()')
            current_element_multiplier = 1
            current_element = compound[:1]
            current_element_multiplier = int(compound[1:3])
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            if len(compound) > 2:
                compound = compound[3:]
            else:
                compound = ""
            print('elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper(): compound = ',
                  compound)
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound is ', current_compound)

    if len(compound) < 3:
        print('if len(compound) < 3:')
        while len(compound) > 0:
            if compound[0] == '_':
                compound = ""
                print("In if compound[0] == '_':")
            elif len(compound) == 1:
                if compound[0].isupper():
                    print('In compound[0].isupper()')
                    current_element_multiplier = 1
                    current_element = compound[0]
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    print('In if compound[0].isupper():: compound = ', compound)
                    print('current_element is ', current_element, ' current_element_multiplier is ',
                          current_element_multiplier)
                    print('current_compound is ', current_compound)
                    compound = ""
            elif len(compound) == 2:
                if compound[0].isupper() and compound[1].isupper():
                    print('In compound[0].isupper() and compound[1].isupper()')
                    current_element_multiplier = 1
                    current_element = compound[0]
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    compound = compound[1:]
                    print('In elif compound[1].isupper() and len(compound) > 1: compound = ', compound)
                    print('current_element is ', current_element, ' current_element_multiplier is ',
                          current_element_multiplier)
                    print('current_compound is ', current_compound)
                elif compound[0].isupper() and compound[1].islower():
                    print('In compound[0].isupper() and compound[1].islower()')
                    current_element_multiplier = 1
                    current_element = compound[0:1]
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    compound = ""
                    print('In if compound[0].isupper() and compound[1].islower():: compound = ', compound)
                    print('current_element is ', current_element, ' current_element_multiplier is ',
                          current_element_multiplier)
                    print('current_compound is ', current_compound)
                elif compound[0].isupper() and compound[1].isdigit():
                    print('In compound[0].isupper() and compound[1].isdigit()')
                    current_element_multiplier = 1
                    current_element = compound[0]
                    current_element_multiplier = int(compound[1])
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    compound = ""
                    print('In if compound[0].isupper() and compound[1].islower():: compound = ', compound)
                    print('current_element is ', current_element, ' current_element_multiplier is ',
                          current_element_multiplier)
                    print('current_compound is ', current_compound)
        print('compound =  ', compound)
        compound = ""
        return current_compound
        #Display_Parsed_Reactant(current_compound)


def Display_Parsed_Reactant(parsed_compound):
    print('Entering Display_Parsed_Compound')
    print(parsed_compound)
    ''' Need to reset all possible product boxes to empty strings'''
    Reset_Product_Boxes()

    e_eci_1_M_qty.delete(0, END)
    e_eci_1_M_qty.insert(0, 1)
    cb_Select_CB4.set('elements')
    element_1 = parsed_compound[0]
    print('element_1 is ', element_1)
    cb_eci_4.set("")
    cb_eci_4_N.set("")
    cb_eci_4.set(element_1)
    moles_1 = parsed_compound[1]
    print('moles_1 is ', moles_1)
    e_eci_4_M_qty.delete(0, END)
    e_eci_4_M_qty.insert(0, moles_1)

    cb_Select_CB5.set('elements')
    element_2 = parsed_compound[2]
    print('element_2 is ', element_2)
    cb_eci_5.set("")
    cb_eci_5_N.set("")
    cb_eci_5.set(element_2)
    moles_2 = parsed_compound[3]
    e_eci_5_M_qty.delete(0, END)
    e_eci_5_M_qty.insert(0, moles_2)

    try:
        if parsed_compound[4]:
            print('parsed_compound[4] is ', parsed_compound[4])
            cb_Select_CB6.set('elements')
            element_3 = parsed_compound[4]
            print('element_3 is ', element_3)
            cb_eci_6.set("")
            cb_eci_6_N.set("")
            cb_eci_6.set(element_3)
            moles_3 = parsed_compound[5]
            e_eci_6_M_qty.delete(0, END)
            e_eci_6_M_qty.insert(0, moles_3)
        if parsed_compound[6]:
            cb_Select_CB3.set('elements')
            element_4 = parsed_compound[6]
            print('element_4 is ', element_4)
            cb_eci_3.set("")
            cb_eci_3_N.set("")
            cb_eci_3.set(element_4)
            moles_4 = parsed_compound[7]
            e_eci_3_M_qty.delete(0, END)
            e_eci_3_M_qty.insert(0, moles_4)
    except:
        pass

def Display_Parsed_Product(parsed_compound):
    print('Entering Display_Parsed_Compound')
    print(parsed_compound)
    ''' Need to reset all possible product boxes to empty strings'''
    Reset_Product_Boxes()
    e_eci_4_M_qty.delete(0, END)
    e_eci_4_M_qty.insert(0, 1)

    cb_Select_CB1.set('elements')
    element_1 = parsed_compound[0]
    print('element_1 is ', element_1)
    cb_eci_1.set("")
    cb_eci_1_N.set("")
    cb_eci_1.set(element_1)
    moles_4 = parsed_compound[1]
    print('moles_1 is ', moles_4)
    e_eci_1_M_qty.delete(0, END)
    e_eci_1_M_qty.insert(0, moles_4)

    cb_Select_CB2.set('elements')
    element_2 = parsed_compound[2]
    print('element_2 is ', element_2)
    cb_eci_2.set("")
    cb_eci_2_N.set("")
    cb_eci_2.set(element_2)
    moles_2 = parsed_compound[3]
    e_eci_2_M_qty.delete(0, END)
    e_eci_2_M_qty.insert(0, moles_2)

    try:
        if parsed_compound[4]:
            print('parsed_compound[4] is ', parsed_compound[4])
            cb_Select_CB3.set('elements')
            element_3 = parsed_compound[4]
            print('element_3 is ', element_3)
            cb_eci_3.set("")
            cb_eci_3_N.set("")
            cb_eci_3.set(element_3)
            moles_3 = parsed_compound[5]
            e_eci_3_M_qty.delete(0, END)
            e_eci_3_M_qty.insert(0, moles_3)
        if parsed_compound[6]:
            cb_Select_CB6.set('elements')
            element_4 = parsed_compound[6]
            print('element_4 is ', element_4)
            cb_eci_6.set("")
            cb_eci_6_N.set("")
            cb_eci_6.set(element_4)
            moles_4 = parsed_compound[7]
            e_eci_6_M_qty.delete(0, END)
            e_eci_6_M_qty.insert(0, moles_4)
    except:
        pass

''' Use decimal instead of float in order to eliminate floating point errors. '''
def Parse_Compound_Logic():
    ''' Identify the logical steps in parsing compounds'''
    print('In Parse_Compound_Logic')
    ''' Get len(compound'''
    ''' If len(compound < 3'''
    ''' If len(compound >= 3 -- there is only one four item pattern, so include it with 3 item pattern. '''
    ''' Patterns that allow the first element to be identified and separated are:'''
    ''' Upper, upper -- compound[0].isupper() and compound[1].isupper()'''
    ''' Upper, lower, upper -- compound[0].isupper() and compound[1].islower() and compound[2].isupper() '''
    ''' Upper, digit, upper -- compound[0].isupper() and compound[1].isdigit() and compound[2].isupper() '''
    ''' Upper, lower, digit -- compound[0].isupper() and compound[1].islower() and compound[2].isdigit() '''
    ''' Patterns that allow the subsequent element or digits to be identified and separated are:'''
    ''' same as above'''
    ''' Upper, upper -- compound[0].isupper() and compound[1].isupper()'''
    ''' Upper, lower, upper -- compound[0].isupper() and compound[1].islower() and compound[2].isupper() '''
    ''' Upper, digit, upper -- compound[0].isupper() and compound[1].isdigit() and compound[2].isupper() '''

    ''' *** Not valid *** Upper, lower, digit -- compound[0].isupper() and compound[1].islower() and compound[2].isdigit() '''
    ''' new patterns'''
    ''' Upper, digit, digit -- compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit() '''
    ''' Upper, lower, digit, digit -- compound[0].isupper() and compound[1].islower() and compound[2].isdigit()  and compound[3].isdigit()'''
    ''' digit, upper -- compound[0].isdigit() and compound[1].isupper() '''
    ''' digit, digit, upper -- compound[0].isdigit() and compound[1].isdigit() and compound[2].isupper() '''
    ''' final patterns'''
    ''' If len(compound < 3'''
    ''' All the above where length is 2, 1, or 0. '''


def CountElements():  # The following does not work. Need valid test for value
    e_Explanation.insert(tk.END, "CountElements process entered\n")
    intElementCount = 0
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    eci_3 = cb_eci_3.get()
    if eci_1 == "":  # cb_eci_1
        pass
    else:
        intElementCount = 1
    if eci_2 == "":
        pass
    else:
        intElementCount = intElementCount + 1
    if eci_3 == "":
        pass
    else:
        intElementCount = intElementCount + 1
    print('element count is', intElementCount)
    # rtb_Explanation.Text = rtb_Explanation.Text & intElementCount

def AlphabetizeElements():  # TypeError: '<' not supported between instances of 'StringVar' and 'StringVar'
    e_Explanation.insert(END, "AlphabetizeElements process entered\n")
    strAlphaElements = ""
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    eci_3 = cb_eci_3.get()

    if eci_1 < eci_2 and eci_1 < eci_3:
        if eci_2 < eci_3:
            strAlphaElements = eci_1 + eci_2 + eci_3
        elif eci_3 < eci_2:
            strAlphaElements = eci_1 + eci_3 + eci_2
    elif eci_2 < eci_1 and eci_2 < eci_3:
        if eci_1 < eci_3:
            strAlphaElements = eci_2 + eci_1 + eci_3
        elif eci_3 < eci_1:
            strAlphaElements = eci_2 + eci_3 + eci_1
    elif eci_3 < eci_1 and eci_3 < eci_2:
        if eci_1 < eci_2:
            strAlphaElements = eci_3 + eci_1 + eci_2
        elif eci_2 < eci_1:
            strAlphaElements = eci_3 + eci_2 + eci_1
    else:
        e_Explanation.insert(END, 'Error:Fell to else clause in AlphabetizeElements\n')
    # e_Explanation.insert(tk.END, 'strAlphaElements is %', strAlphaElements) #How do I insert arguments?
    print('strAlphaElements is ', strAlphaElements)



'''Create the GUI '''
#root.title('Chemistry')

titlefont = ('Ariel', 14, 'bold')
labelfont = ('Ariel', 14)  # , 'bold')
buttonfont = ('Ariel', 12)  # , 'bold')
entryfont = ('Ariel', 12)  # , 'bold')
font1 = font.Font(name='TkCaptionFont', exists=True)
font1.config(family='courier new', size=20)

winInstructions = Toplevel()
e_Instructions = Text(winInstructions, height=20, width=50)
e_Instructions.grid(row=0, column=0) #, columnspan=6, sticky=W)
e_Instructions.config(font=entryfont)
e_Instructions.insert(END, "Program instructions will be provided in this window. \n")
e_Instructions.insert(END, "Move this window so it is always visible, or minimize it are resize it as needed. \n")
e_Instructions.insert(END, "Process instructions will be provided in this window. \n")

lbl_Title = Label(inside_frame, text="Chemistry")
lbl_Title.grid(row=0, column=3)
lbl_Title.config(font=titlefont)

lbl_blank = Label(inside_frame, text="")
lbl_blank.grid(row=1, column=0)
lbl_blank.config(font=labelfont)

lbl_record_create = Label(inside_frame, text="Create record:")
lbl_record_create.grid(row=2, column=0)
lbl_record_create.config(font=labelfont)
e_recordname = Entry(inside_frame, text="")
e_recordname.grid(row=2, column=1, columnspan=2)
e_recordname.config(font=labelfont)
btn_create_record = Button(inside_frame, text='Create Record', command=create_record)
btn_create_record.grid(row=2, column=3)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", create_record())
btn_update_record = Button(inside_frame, text='Update Record', command=update_record)
btn_update_record.grid(row=2, column=4)
btn_update_record.config(font=buttonfont)
btn_update_record.bind("<<ComboboxSelected>>", update_record)
btn_Continue = Button(inside_frame, text='* Continue *', command=Continue)
btn_Continue.grid(row=2, column=5)
btn_Continue.config(font=titlefont)

lbl_record_ops = Label(inside_frame, text="Get record:")
lbl_record_ops.grid(row=3, column=0)
lbl_record_ops.config(font=labelfont)
cb_RecordName: Combobox = Combobox(inside_frame, values="", width=12)
cb_RecordName.grid(row=3, column=1)
cb_RecordName.config(font=entryfont)
cb_RecordName.bind("<<ComboboxSelected>>", retrieve_record)
# e_recordname = Entry(root, text="")   #, width=30)
# e_recordname.grid(row=3, column=3)
# e_recordname.config(font=labelfont)
btn_create_record = Button(inside_frame, text='Get Record', command=get_record)
btn_create_record.grid(row=3, column=2)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", retrieve_record)
btn_create_record = Button(inside_frame, text='Previous Record', command=get_record)
btn_create_record.grid(row=3, column=3)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", previous_record)
btn_create_record = Button(inside_frame, text='Next Record', command=get_record)
btn_create_record.grid(row=3, column=4)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", next_record)
btn_show_instructions = Button(inside_frame, text='Show Instructions', command=get_record)
btn_show_instructions.grid(row=2, column=6)
btn_show_instructions.config(font=labelfont)
#btn_show_instructions.bind("<<ComboboxSelected>>", show_hide_instructions)

lbl_LU_Compound = Label(inside_frame, text="   Look up compound:")
lbl_LU_Compound.grid(row=6, column=0)
lbl_LU_Compound.config(font=labelfont)
cb_LU_Compound = Combobox(inside_frame, values=compound_formula_string, width=12)
cb_LU_Compound.grid(row=6, column=1)
cb_LU_Compound.config(font=entryfont)

# Create a search for and retrieve a compount
lbl_LU_Process = Label(inside_frame, text="   Look up process:")
lbl_LU_Process.grid(row=6, column=2)
lbl_LU_Process.config(font=labelfont)
cb_LU_Process = Combobox(inside_frame, values=major_process_list, width=12)
cb_LU_Process.grid(row=6, column=3)
cb_LU_Process.config(font=entryfont)
# Create a search for and retrieve a process
lbl_LU_Environment = Label(inside_frame, text="   Look up environment:", width=22)
lbl_LU_Environment.grid(row=6, column=4)
lbl_LU_Environment.config(font=labelfont)
cb_LU_Environment = Combobox(inside_frame, values=environment, width=12)
cb_LU_Environment.grid(row=6, column=5)
cb_LU_Environment.config(font=entryfont)

lbl_Select_M_Process = Label(inside_frame, text="   Select major process", width=20)
lbl_Select_M_Process.grid(row=7, column=0)
lbl_Select_M_Process.config(font=labelfont)
cb_Select_M_Process: Combobox = Combobox(inside_frame, values=major_process_list, textvariable=major_process_selected, width=12)
cb_Select_M_Process.grid(row=7, column=1)
cb_Select_M_Process.config(font=entryfont)
lbl_Select_m_Process = Label(inside_frame, text="   Select minor process", width=20)
lbl_Select_m_Process.grid(row=7, column=2)
lbl_Select_m_Process.config(font=labelfont)
cb_Select_m_Process: Combobox = Combobox(inside_frame, values=minor_process_list, textvariable=minor_process_selected, width=12)
cb_Select_m_Process.grid(row=7, column=3)
cb_Select_m_Process.config(font=entryfont)
cb_Select_m_Process.bind("<<ComboboxSelected>>", minor_process_selected)
lbl_Select_Environment = Label(inside_frame, text="   Select environment:", width=22)
lbl_Select_Environment.grid(row=7, column=4)
lbl_Select_Environment.config(font=titlefont)
cb_Select_Environment: Combobox = Combobox(inside_frame, values=environment, width=12)
cb_Select_Environment.grid(row=7, column=5)
cb_Select_Environment.config(font=entryfont)

lbl_blank = Label(inside_frame, text="")
lbl_blank.grid(row=8, column=0)

lbl_eci_1 = Label(inside_frame, text="   Select Element, Compound or Ion for ComboBox 1")
lbl_eci_1.grid(row=9, column=0, columnspan=3) #, sticky=W)
lbl_eci_1.config(font=labelfont)
cb_Select_CB1: Combobox = Combobox(inside_frame, values=eci_cb_values, width=10)
cb_Select_CB1.grid(row=9, column=3) #, sticky=W)
cb_Select_CB1.config(font=entryfont)
cb_Select_CB1.bind("<<ComboboxSelected>>", select_eci_1_type)
# cb_Select_CB1.bind("<<ComboboxSelected>>", callback1)
# cb_Process = Combobox(root, values=process_list, width=20)
# cb_Process.grid(row=9, column=3) # , columnspan=2
# cb_Process.config(font=entryfont)
lbl_eci_4 = Label(inside_frame, text="Select Element, Compound or Ion for ComboBox 4")
lbl_eci_4.grid(row=9, column=4, columnspan=3) #, sticky=W)
lbl_eci_4.config(font=labelfont)
cb_Select_CB4 = Combobox(inside_frame, values=eci_cb_values, width=10)
cb_Select_CB4.grid(row=9, column=7)
cb_Select_CB4.config(font=entryfont)
cb_Select_CB4.bind("<<ComboboxSelected>>", select_eci_4_type)

lbl_eci_1_qty = Label(inside_frame, text="ECI Qty 1", width=8)
lbl_eci_1_qty.grid(row=11, column=0)
lbl_eci_1_qty.config(font=labelfont)
lbl_eci_1_units = Label(inside_frame, text="Units 1", width=10)
lbl_eci_1_units.grid(row=11, column=1) #, sticky=W)
lbl_eci_1_units.config(font=labelfont)
lbl_eci_1 = Label(inside_frame, text="ECI 1", width=10)
lbl_eci_1.grid(row=11, column=2) #, sticky=W)
lbl_eci_1.config(font=labelfont)
lbl_eci_1_valence = Label(inside_frame, text="Valence 1", width=10)
lbl_eci_1_valence.grid(row=11, column=3) #, sticky=W)
lbl_eci_1_valence.config(font=labelfont)
lbl_eci_4_qty = Label(inside_frame, text="ECI Qty 4", width=8)
lbl_eci_4_qty.grid(row=11, column=4)
lbl_eci_4_qty.config(font=labelfont)
lbl_eci_4_units = Label(inside_frame, text="Units 4", width=10)
lbl_eci_4_units.grid(row=11, column=5) #, sticky=W)
lbl_eci_4_units.config(font=labelfont)
lbl_eci_4 = Label(inside_frame, text="ECI 4", width=10)
lbl_eci_4.grid(row=11, column=6) #, sticky=W)
lbl_eci_4.config(font=labelfont)
lbl_eci_4_valence = Label(inside_frame, text="Valence 4", width=10)
lbl_eci_4_valence.grid(row=11, column=7) #, sticky=W)
lbl_eci_4_valence.config(font=labelfont)
lbl_eci_4_Molar_Mass_Label = Label(inside_frame, text="Molar Mass", width=10)
lbl_eci_4_Molar_Mass_Label.grid(row=11, column=8) #, sticky=W)
lbl_eci_4_Molar_Mass_Label.config(font=labelfont)

e_eci_1_qty = Entry(inside_frame, text="", textvariable=eci_1_qty, width=8)
e_eci_1_qty.grid(row=12, column=0)
e_eci_1_qty.config(font=entryfont)
e_eci_1_qty.bind('<Return>', eci_1_qty_adjusted)
#e_eci_1_qty = 666
#e_eci_1_qty = 36.0
''' Can I generalize the following to: set_eci_db_eci_1_qty = e_eci_1_qty.get()'''
#e_eci_1_qty.bind('<FocusOut>', lambda event: set_eci_db_eci_1_qty(e_eci_1_qty.get()))
cb_eci_1_units: Combobox = Combobox(inside_frame, values=unit_values, textvariable=eci_1_units, width=10)
cb_eci_1_units.grid(row=12, column=1)
cb_eci_1_units.config(font=entryfont)
cb_eci_1_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_1: Combobox = Combobox(inside_frame, textvariable=eci_1, width=12)
cb_eci_1.grid(row=12, column=2)
cb_eci_1.config(font=labelfont)
cb_eci_1['values'] = element_symbol_string
cb_eci_1.bind("<<ComboboxSelected>>", setSelectedItemName)

cb_eci_1_valence: Combobox = Combobox(inside_frame, textvariable=eci_1_valence, width=8)
cb_eci_1_valence.grid(row=12, column=3)
cb_eci_1_valence.config(font=entryfont)
cb_eci_1_valence['values'] = valences
e_eci_4_qty = Entry(inside_frame, text="", textvariable=eci_4_qty, width=8)
e_eci_4_qty.grid(row=12, column=4)
e_eci_4_qty.config(font=entryfont)
cb_eci_4_units: Combobox = Combobox(inside_frame, values=unit_values, textvariable=eci_4_units, width=10)
cb_eci_4_units.grid(row=12, column=5)
cb_eci_4_units.config(font=entryfont)
cb_eci_4_units.bind("<<ComboboxSelected>>", eci_units_selected)
# cb_eci_4_units.bind("<<ComboboxSelected>>", callback_eci_4_units)
cb_eci_4: Combobox = Combobox(inside_frame, textvariable=eci_4, width=12)
cb_eci_4.grid(row=12, column=6)
cb_eci_4.config(font=entryfont)
cb_eci_4['values'] = compound_formula_string
cb_eci_4.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_4_valence: Combobox = Combobox(inside_frame, textvariable=eci_4_valence, width=5)
cb_eci_4_valence.grid(row=12, column=7)
cb_eci_4_valence.config(font=entryfont)
cb_eci_4_valence['values'] = valences
lbl_eci_4_Molar_Mass_Qty_label = Label(inside_frame, text="Qty here", width=10)
lbl_eci_4_Molar_Mass_Qty_label.grid(row=12, column=8) #, sticky=W)
lbl_eci_4_Molar_Mass_Qty_label.config(font=labelfont)

e_eci_1_M_qty = Entry(inside_frame, text="", textvariable=eci_1_M_qty, width=8)
e_eci_1_M_qty.grid(row=13, column=0)
e_eci_1_M_qty.config(font=entryfont)
e_eci_1_M_qty.bind('<Return>', eci_1_M_qty_adjusted)
#e_eci_1_M_qty.bind('<FocusOut>', (lambda event: check_entry_changes()))  # '''  does not work'''
lbl_eci_1_units_M = Label(inside_frame, text="Moles", width=12)
lbl_eci_1_units_M.grid(row=13, column=1)
lbl_eci_1_units_M.config(font=labelfont)
# cb_Elements1 = Combobox(root, values=elements, width=30)
cb_eci_1_N: Combobox = Combobox(inside_frame, textvariable=eci_1_name, width=12)
cb_eci_1_N.grid(row=13, column=2)
cb_eci_1_N.config(font=entryfont)
cb_eci_1_N['values'] = compound_name_string
cb_eci_1_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

e_eci_4_M_qty = Entry(inside_frame, text="", textvariable=eci_4_M_qty, width=8)
e_eci_4_M_qty.grid(row=13, column=4)
e_eci_4_M_qty.config(font=entryfont)
lbl_eci_4_units_M = Label(inside_frame, text="Moles", width=10)
lbl_eci_4_units_M.grid(row=13, column=5)
lbl_eci_4_units_M.config(font=labelfont)
cb_eci_4_N: Combobox = Combobox(inside_frame, values=compound_formula_string, textvariable=eci_4_name, width=12)
cb_eci_4_N.grid(row=13, column=6)
cb_eci_4_N.config(font=entryfont)
cb_eci_4_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)
lbl_eci_4_Alpha_Label = Label(inside_frame, text="Alpha", width=10)
lbl_eci_4_Alpha_Label.grid(row=13, column=8) #, sticky=W)
lbl_eci_4_Alpha_Label.config(font=labelfont)

lbl_Temp_Units_1 = Label(inside_frame, text="Temp Units", width=10)
lbl_Temp_Units_1.grid(row=14, column=0)
lbl_Temp_Units_1.config(font=labelfont)

lbl_Temp_Qty_1 = Label(inside_frame, text="Temp Qty", width=10)
lbl_Temp_Qty_1.grid(row=14, column=1)
lbl_Temp_Qty_1.config(font=labelfont)
lbl_Press_Units_1 = Label(inside_frame, text="Press Units", width=10)
lbl_Press_Units_1.grid(row=14, column=2) #, sticky=W)
lbl_Press_Units_1.config(font=labelfont)
lbl_Press_Qty_1 = Label(inside_frame, text="Press Qty", width=10)
lbl_Press_Qty_1.grid(row=14, column=3) #, sticky=W)
lbl_Press_Qty_1.config(font=labelfont)
lbl_Temp_Units_4 = Label(inside_frame, text="Temp Units", width=10)
lbl_Temp_Units_4.grid(row=14, column=4)
lbl_Temp_Units_4.config(font=labelfont)
lbl_Temp_Qty_4 = Label(inside_frame, text="Temp Qty", width=10)
lbl_Temp_Qty_4.grid(row=14, column=5) #, sticky=W)
lbl_Temp_Qty_4.config(font=labelfont)
lbl_Press_Units_4 = Label(inside_frame, text="Press Units", width=10)
lbl_Press_Units_4.grid(row=14, column=6) #, sticky=W)
lbl_Press_Units_4.config(font=labelfont)
lbl_Press_Qty_4 = Label(inside_frame, text="Press Qty", width=10)
lbl_Press_Qty_4.grid(row=14, column=7) #, sticky=W)
lbl_Press_Qty_4.config(font=labelfont)
e_4_Alpha = Entry(inside_frame, text="", textvariable=alpha_4, width=10)
e_4_Alpha.grid(row=14, column=8)
e_4_Alpha.config(font=entryfont)
#e_4_Alpha.bind('<Return>', eci_1_Temp_qty_adjusted)

cb_1_Temp_Units: Combobox = Combobox(inside_frame, values=temp_units, textvariable=eci_1_temp_units,
                                     width=10)  # eci_temp_1_units
cb_1_Temp_Units.grid(row=15, column=0)
cb_1_Temp_Units.config(font=entryfont)
cb_1_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_temp_units)
e_Temp_Qty_1 = Entry(inside_frame, text="", textvariable=eci_temp_1_qty, width=8)
e_Temp_Qty_1.grid(row=15, column=1)
e_Temp_Qty_1.config(font=entryfont)
e_Temp_Qty_1.bind('<Return>', eci_1_Temp_qty_adjusted)
cb_1_Press_Units: Combobox = Combobox(inside_frame, values=press_units, textvariable=eci_1_press_units, width=10)
cb_1_Press_Units.grid(row=15, column=2)  # , padx=4)
cb_1_Press_Units.config(font=entryfont)
cb_1_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_press_units)
e_Press_Qty_1 = Entry(inside_frame, text="", textvariable=eci_press_1_qty, width=8)
e_Press_Qty_1.grid(row=15, column=3)
e_Press_Qty_1.config(font=entryfont)
cb_4_Temp_Units: Combobox = Combobox(inside_frame, values=temp_units, textvariable=eci_4_temp_units, width=10)
cb_4_Temp_Units.grid(row=15, column=4)
cb_4_Temp_Units.config(font=entryfont)
cb_4_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Temp_Qty_4 = Entry(inside_frame, text="", textvariable=eci_temp_4_qty, width=8)
e_Temp_Qty_4.grid(row=15, column=5) #, sticky=W)
e_Temp_Qty_4.config(font=entryfont)
cb_4_Press_Units: Combobox = Combobox(inside_frame, values=press_units, textvariable=eci_4_press_units, width=10)
cb_4_Press_Units.grid(row=15, column=6)
cb_4_Press_Units.config(font=entryfont)
cb_4_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Press_Qty_4 = Entry(inside_frame, text="", textvariable=eci_press_4_qty, width=8)
e_Press_Qty_4.grid(row=15, column=7)
e_Press_Qty_4.config(font=entryfont)
lbl_eci_4_Charge_Label = Label(inside_frame, text="Ion charge", width=10)
lbl_eci_4_Charge_Label.grid(row=15, column=8) #, sticky=W)
lbl_eci_4_Charge_Label.config(font=labelfont)

lbl_blank = Label(inside_frame, text="")
lbl_blank.grid(row=16, column=0)
lbl_blank.config(font=labelfont)


_4_Charge = Entry(inside_frame, text="", textvariable=ion_4_charge, width=10)
_4_Charge.grid(row=16, column=8)
_4_Charge.config(font=entryfont)
#lbl_blank = Label(inside_frame, text="")
#lbl_blank.grid(row=16, column=0)
#lbl_blank.config(font=labelfont)

lbl_eci_2 = Label(inside_frame, text="   Select Element, Compound or Ion for ComboBox 2")
lbl_eci_2.grid(row=17, column=0, columnspan=3) #, sticky=W)
lbl_eci_2.config(font=labelfont)
cb_Select_CB2: Combobox = Combobox(inside_frame, values=eci_cb_values, width=10)
cb_Select_CB2.grid(row=17, column=3) #, sticky=W)
cb_Select_CB2.config(font=entryfont)
cb_Select_CB2.bind("<<ComboboxSelected>>", select_eci_2_type)
# btn_Select_CB2 = Button(root, command=Synthesis(variables), text = 'Elements')
# btn_Select_CB2.grid(row=17, column=2)
# btn_Select_CB2.config(font=buttonfont)
lbl_eci_5 = Label(inside_frame, text="Select Element, Compound or Ion for ComboBox 5")
lbl_eci_5.grid(row=17, column=4, columnspan=2) #, sticky=W)
lbl_eci_5.config(font=labelfont)
cb_Select_CB5: Combobox = Combobox(inside_frame, values=eci_cb_values, width=10)  # , width=20)
cb_Select_CB5.grid(row=17, column=6)
cb_Select_CB5.config(font=entryfont)
cb_Select_CB5.bind("<<ComboboxSelected>>", select_eci_5_type)

lbl_eci_2_qty = Label(inside_frame, text="ECI Qty 2", width=10)
lbl_eci_2_qty.grid(row=19, column=0)
lbl_eci_2_qty.config(font=labelfont)
lbl_eci_2_units = Label(inside_frame, text="Units 2", width=10)
lbl_eci_2_units.grid(row=19, column=1) #, sticky=W)
lbl_eci_2_units.config(font=labelfont)
lbl_eci_2 = Label(inside_frame, text="ECI 2")
lbl_eci_2.grid(row=19, column=2) #, sticky=W)
lbl_eci_2.config(font=labelfont)
lbl_eci_2_valence = Label(inside_frame, text="Valence 2", width=10)
lbl_eci_2_valence.grid(row=19, column=3) #, sticky=W)
lbl_eci_2_valence.config(font=labelfont)
lbl_eci_5_qty = Label(inside_frame, text="ECI Qty 5", width=10)
lbl_eci_5_qty.grid(row=19, column=4)
lbl_eci_5_qty.config(font=labelfont)
lbl_eci_5_units = Label(inside_frame, text="Units 5", width=10)
lbl_eci_5_units.grid(row=19, column=5)
lbl_eci_5_units.config(font=labelfont)
lbl_eci_5 = Label(inside_frame, text="ECI 5", width=10)
lbl_eci_5.grid(row=19, column=6)
lbl_eci_5.config(font=labelfont)
lbl_eci_5_valence = Label(inside_frame, text="Valence 5", width=10)
lbl_eci_5_valence.grid(row=19, column=7) #, sticky=W)
lbl_eci_5_valence.config(font=labelfont)

e_eci_2_qty = Entry(inside_frame, text="", textvariable=eci_2_qty, width=8)
e_eci_2_qty.grid(row=20, column=0)
e_eci_2_qty.config(font=entryfont)
e_eci_2_qty.bind('<Return>', eci_2_qty_adjusted)
# cb_Elements1.bind("<<ComboboxSelected>>", callback_E1)
cb_eci_2_units: Combobox = Combobox(inside_frame, values=unit_values, textvariable=eci_2_units, width=10)
cb_eci_2_units.grid(row=20, column=1)
cb_eci_2_units.config(font=entryfont)
cb_eci_2_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_2: Combobox = Combobox(inside_frame, textvariable=eci_2, width=12)
cb_eci_2.grid(row=20, column=2)
cb_eci_2.config(font=entryfont)
cb_eci_2['values'] = element_symbol_string
cb_eci_2.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_2_valence: Combobox = Combobox(inside_frame, textvariable=eci_2_valence, width=8)
cb_eci_2_valence.grid(row=20, column=3)
cb_eci_2_valence.config(font=entryfont)
cb_eci_2_valence['values'] = valences
e_eci_5_qty = Entry(inside_frame, text="", textvariable=eci_5_qty, width=8)
e_eci_5_qty.grid(row=20, column=4)
e_eci_5_qty.config(font=entryfont)
cb_eci_5_units: Combobox = Combobox(inside_frame, values=unit_values, textvariable=eci_5_units, width=10)
cb_eci_5_units.grid(row=20, column=5)
cb_eci_5_units.config(font=entryfont)
cb_eci_5_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_5: Combobox = Combobox(inside_frame, values=compound_formula_string, textvariable=eci_5, width=12)
cb_eci_5.grid(row=20, column=6)
cb_eci_5.config(font=entryfont)
cb_eci_5.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_5_valence: Combobox = Combobox(inside_frame, textvariable=eci_5_valence, width=5)
cb_eci_5_valence.grid(row=20, column=7)
cb_eci_5_valence.config(font=entryfont)
cb_eci_5_valence['values'] = valences

'''    e_eci_2_M_qty.delete(0)
UnboundLocalError: local variable 'e_eci_2_M_qty' referenced before assignment
'''
# e_eci_2_M_qty = Entry(root, text="", textvariable=eci_2_M_qty, width=8)
# e_eci_1_M_qty.grid(row=13, column=0)
# e_eci_1_M_qty.config(font=entryfont)
e_eci_2_M_qty = Entry(inside_frame, text="", textvariable=eci_2_M_qty, width=8)
e_eci_2_M_qty.grid(row=21, column=0)
e_eci_2_M_qty.config(font=entryfont)
e_eci_2_M_qty.bind('<Return>', eci_2_M_qty_adjusted)
lbl_eci_2_units_M = Label(inside_frame, text="Moles", width=10)
lbl_eci_2_units_M.grid(row=21, column=1)
lbl_eci_2_units_M.config(font=labelfont)
cb_eci_2_N: Combobox = Combobox(inside_frame, values=elements_name_list, textvariable=eci_2_name, width=12)
cb_eci_2_N.grid(row=21, column=2)
cb_eci_2_N.config(font=entryfont)
cb_eci_2_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)
e_eci_5_M_qty = Entry(inside_frame, text="CompoundQty 5", textvariable=eci_5_M_qty, width=8)
e_eci_5_M_qty.grid(row=21, column=4)
e_eci_5_M_qty.config(font=entryfont)
lbl_eci_5_units_M = Label(inside_frame, text="Moles", width=10)
lbl_eci_5_units_M.grid(row=21, column=5)
lbl_eci_5_units_M.config(font=labelfont)
cb_eci_5_N: Combobox = Combobox(inside_frame, values=compound_name_string, textvariable=eci_5_name, width=12)
cb_eci_5_N.grid(row=21, column=6)
cb_eci_5_N.config(font=entryfont)
cb_eci_5_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

lbl_Temp_Units_2 = Label(inside_frame, text="Temp Units", width=10)
lbl_Temp_Units_2.grid(row=22, column=0)
lbl_Temp_Units_2.config(font=labelfont)
lbl_Temp_Qty_2 = Label(inside_frame, text="Temp Qty", width=10)
lbl_Temp_Qty_2.grid(row=22, column=1)
lbl_Temp_Qty_2.config(font=labelfont)
lbl_Press_Units_2 = Label(inside_frame, text="Press Units", width=10)
lbl_Press_Units_2.grid(row=22, column=2)
lbl_Press_Units_2.config(font=labelfont)
lbl_Press_Qty_2 = Label(inside_frame, text="Press Qty", width=10)
lbl_Press_Qty_2.grid(row=22, column=3)
lbl_Press_Qty_2.config(font=labelfont)
lbl_Temp_Units_5 = Label(inside_frame, text="Temp Units", width=10)
lbl_Temp_Units_5.grid(row=22, column=4)
lbl_Temp_Units_5.config(font=labelfont)
lbl_Temp_Qty_5 = Label(inside_frame, text="Temp Qty", width=10)
lbl_Temp_Qty_5.grid(row=22, column=5) #, sticky=W)
lbl_Temp_Qty_5.config(font=labelfont)
lbl_Press_Units_5 = Label(inside_frame, text="Press Units", width=10)
lbl_Press_Units_5.grid(row=22, column=6)
lbl_Press_Units_5.config(font=labelfont)
lbl_Press_Qty_5 = Label(inside_frame, text="Press Qty", width=10)
lbl_Press_Qty_5.grid(row=22, column=7)
lbl_Press_Qty_5.config(font=labelfont)

cb_2_Temp_Units: Combobox = Combobox(inside_frame, values=temp_units, textvariable=eci_2_temp_units, width=10)
cb_2_Temp_Units.grid(row=23, column=0)
cb_2_Temp_Units.config(font=entryfont)
cb_2_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Temp_Qty_2 = Entry(inside_frame, text="", textvariable=eci_temp_2_qty, width=8)
e_Temp_Qty_2.grid(row=23, column=1)
e_Temp_Qty_2.config(font=entryfont)
cb_2_Press_Units: Combobox = Combobox(inside_frame, values=press_units, textvariable=eci_2_press_units, width=10)
cb_2_Press_Units.grid(row=23, column=2)
cb_2_Press_Units.config(font=entryfont)
cb_2_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Press_Qty_2 = Entry(inside_frame, text="", textvariable=eci_press_2_qty, width=8)
e_Press_Qty_2.grid(row=23, column=3)
e_Press_Qty_2.config(font=entryfont)
cb_5_Temp_Units: Combobox = Combobox(inside_frame, values=temp_units, textvariable=eci_5_temp_units, width=10)
cb_5_Temp_Units.grid(row=23, column=4)
cb_5_Temp_Units.config(font=entryfont)
cb_5_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Temp_Qty_5 = Entry(inside_frame, text="", textvariable=eci_temp_2_qty, width=8)
e_Temp_Qty_5.grid(row=23, column=5) #, sticky=W)
e_Temp_Qty_5.config(font=entryfont)
cb_5_Press_Units: Combobox = Combobox(inside_frame, values=press_units, textvariable=eci_5_press_units, width=10)
cb_5_Press_Units.grid(row=23, column=6)
cb_5_Press_Units.config(font=entryfont)
cb_5_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Press_Qty_5 = Entry(inside_frame, text="", textvariable=eci_press_5_qty, width=8)
e_Press_Qty_5.grid(row=23, column=7)
e_Press_Qty_5.config(font=entryfont)

lbl_blank = Label(inside_frame, text="")
lbl_blank.grid(row=24, column=0)
lbl_blank.config(font=labelfont)

lbl_eci_3 = Label(inside_frame, text="   Select Element, Compound or Ion for ComboBox 3")
lbl_eci_3.grid(row=26, column=0, columnspan=3) #, sticky=W)
lbl_eci_3.config(font=labelfont)
cb_Select_CB3: Combobox = Combobox(inside_frame, values=eci_cb_values, width=10)
cb_Select_CB3.grid(row=26, column=3) #, sticky=W)
cb_Select_CB3.config(font=entryfont)
cb_Select_CB3.bind("<<ComboboxSelected>>", select_eci_3_type)
lbl_eci_6 = Label(inside_frame, text="Select Element, Compound or Ion for ComboBox 6 ")
lbl_eci_6.grid(row=26, column=4, columnspan=2) #, sticky=W)
lbl_eci_6.config(font=labelfont)
cb_Select_CB6: Combobox = Combobox(inside_frame, values=eci_cb_values, width=10)
cb_Select_CB6.grid(row=26, column=6) #, sticky=W)
cb_Select_CB6.config(font=entryfont)
cb_Select_CB6.bind("<<ComboboxSelected>>", select_eci_6_type)

lbl_eci_3_qty = Label(inside_frame, text="ECI Qty 3", width=8)
lbl_eci_3_qty.grid(row=27, column=0)
lbl_eci_3_qty.config(font=labelfont)
lbl_eci_3_units = Label(inside_frame, text="Units 3", width=6)
lbl_eci_3_units.grid(row=27, column=1) #, sticky=W)
lbl_eci_3_units.config(font=labelfont)
lbl_eci_3 = Label(inside_frame, text="ECI 3")
lbl_eci_3.grid(row=27, column=2) #, sticky=W)
lbl_eci_3.config(font=labelfont)
lbl_eci_3_valence = Label(inside_frame, text="Valence 3", width=10)
lbl_eci_3_valence.grid(row=27, column=3) #, sticky=W)
lbl_eci_3_valence.config(font=labelfont)
lbl_eci_6_qty = Label(inside_frame, text="ECI Qty 6", width=8)
lbl_eci_6_qty.grid(row=27, column=4)
lbl_eci_6_qty.config(font=labelfont)
lbl_eci_6_units = Label(inside_frame, text="Units 6", width=8)
lbl_eci_6_units.grid(row=27, column=5) #, sticky=W)
lbl_eci_6_units.config(font=labelfont)
lbl_eci_6 = Label(inside_frame, text="ECI 6", width=10)
lbl_eci_6.grid(row=27, column=6) #, sticky=W)
lbl_eci_6.config(font=labelfont)
lbl_eci_6_valence = Label(inside_frame, text="Valence 6", width=10)
lbl_eci_6_valence.grid(row=27, column=7) #, sticky=W)
lbl_eci_6_valence.config(font=labelfont)

e_eci_3_qty = Entry(inside_frame, text="", textvariable=eci_3_qty, width=8)
e_eci_3_qty.grid(row=28, column=0)
e_eci_3_qty.config(font=entryfont)
e_eci_3_qty.bind('<Return>', eci_3_qty_adjusted)
# cb_Elements1.bind("<<ComboboxSelected>>", callback_E1)
cb_eci_3_units: Combobox = Combobox(inside_frame, values=unit_values, textvariable=eci_3_units, width=8)
cb_eci_3_units.grid(row=28, column=1) #, sticky=W)
cb_eci_3_units.config(font=entryfont)
cb_eci_3_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_3: Combobox = Combobox(inside_frame, textvariable=eci_3, width=12)
cb_eci_3.grid(row=28, column=2) #, sticky=W)
cb_eci_3.config(font=entryfont)
cb_eci_3['values'] = element_symbol_string
cb_eci_3.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_3_valence: Combobox = Combobox(inside_frame, textvariable=eci_3_valence, width=8)
cb_eci_3_valence.grid(row=28, column=3)
cb_eci_3_valence.config(font=entryfont)
cb_eci_3_valence['values'] = valences
e_eci_6_qty = Entry(inside_frame, text="", textvariable=eci_6_qty, width=8)
e_eci_6_qty.grid(row=28, column=4)
e_eci_6_qty.config(font=entryfont)
cb_eci_6_units: Combobox = Combobox(inside_frame, values=unit_values, textvariable=eci_6_units, width=8)
cb_eci_6_units.grid(row=28, column=5)
cb_eci_6_units.config(font=entryfont)
cb_eci_6_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_6: Combobox = Combobox(inside_frame, values=compound_formula_string, textvariable=eci_6, width=12)
cb_eci_6.grid(row=28, column=6)
cb_eci_6.config(font=entryfont)
cb_eci_6.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_6_valence: Combobox = Combobox(inside_frame, textvariable=eci_6_valence, width=5)
cb_eci_6_valence.grid(row=28, column=7)
cb_eci_6_valence.config(font=entryfont)
cb_eci_6_valence['values'] = valences

e_eci_3_M_qty = Entry(inside_frame, text=" ", width=8)
e_eci_3_M_qty.grid(row=29, column=0)
e_eci_3_M_qty.config(font=entryfont, textvariable=eci_3_M_qty)
e_eci_3_M_qty.bind('<Return>', eci_3_M_qty_adjusted)
lbl_eci_3_units_M = Label(inside_frame, text="Moles", width=8)
lbl_eci_3_units_M.grid(row=29, column=1)
lbl_eci_3_units_M.config(font=labelfont)
cb_eci_3_N: Combobox = Combobox(inside_frame, values=elements_name_list, textvariable=eci_3_name, width=12)
cb_eci_3_N.grid(row=29, column=2)
cb_eci_3_N.config(font=entryfont)
cb_eci_3_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)
e_eci_6_M_qty = Entry(inside_frame, text="CompoundQty 6", textvariable=eci_6_M_qty, width=8)
e_eci_6_M_qty.grid(row=29, column=4)
e_eci_6_M_qty.config(font=entryfont)
lbl_eci_6_units_M = Label(inside_frame, text="Moles", width=8)
lbl_eci_6_units_M.grid(row=29, column=5)
lbl_eci_6_units_M.config(font=labelfont)
cb_eci_6_N: Combobox = Combobox(inside_frame, values=compound_name_string, textvariable=eci_6_name, width=12)
cb_eci_6_N.grid(row=29, column=6)
cb_eci_6_N.config(font=entryfont)
cb_eci_6_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

lbl_Temp_Units_3 = Label(inside_frame, text="Temp Units", width=10)
lbl_Temp_Units_3.grid(row=30, column=0)
lbl_Temp_Units_3.config(font=labelfont)
lbl_Temp_Qty_3 = Label(inside_frame, text="Temp Qty", width=10)
lbl_Temp_Qty_3.grid(row=30, column=1)
lbl_Temp_Qty_3.config(font=labelfont)
lbl_Press_Units_3 = Label(inside_frame, text="Press Units", width=10)
lbl_Press_Units_3.grid(row=30, column=2)
lbl_Press_Units_3.config(font=labelfont)
lbl_Press_Qty_3 = Label(inside_frame, text="Press Qty", width=10)
lbl_Press_Qty_3.grid(row=30, column=3)
lbl_Press_Qty_3.config(font=labelfont)
lbl_Temp_Units_6 = Label(inside_frame, text="Temp Units", width=10)
lbl_Temp_Units_6.grid(row=30, column=4)
lbl_Temp_Units_6.config(font=labelfont)
lbl_Temp_Qty_6 = Label(inside_frame, text="Temp Qty", width=10)
lbl_Temp_Qty_6.grid(row=30, column=5)
lbl_Temp_Qty_6.config(font=labelfont)
lbl_Press_Units_6 = Label(inside_frame, text="Press Units", width=10)
lbl_Press_Units_6.grid(row=30, column=6)
lbl_Press_Units_6.config(font=labelfont)
lbl_Press_Qty_6 = Label(inside_frame, text="Press Qty", width=10)
lbl_Press_Qty_6.grid(row=30, column=7)
lbl_Press_Qty_6.config(font=labelfont)

cb_3_Temp_Units: Combobox = Combobox(inside_frame, values=temp_units, textvariable=eci_3_temp_units, width=10)
cb_3_Temp_Units.grid(row=31, column=0)
cb_3_Temp_Units.config(font=entryfont)
cb_3_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Temp_Qty_3 = Entry(inside_frame, text="", textvariable=eci_temp_3_qty, width=8)
e_Temp_Qty_3.grid(row=31, column=1)
e_Temp_Qty_3.config(font=entryfont)
cb_3_Press_Units: Combobox = Combobox(inside_frame, values=press_units, textvariable=eci_3_press_units, width=10)
cb_3_Press_Units.grid(row=31, column=2)
cb_3_Press_Units.config(font=entryfont)
cb_3_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Press_Qty_3 = Entry(inside_frame, text="", textvariable=eci_press_3_qty, width=8)
e_Press_Qty_3.grid(row=31, column=3)
e_Press_Qty_3.config(font=entryfont)
cb_6_Temp_Units: Combobox = Combobox(inside_frame, values=temp_units, textvariable=eci_6_temp_units, width=10)
cb_6_Temp_Units.grid(row=31, column=4)
cb_6_Temp_Units.config(font=entryfont)
cb_6_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Temp_Qty_6 = Entry(inside_frame, text="", textvariable=eci_temp_6_qty, width=8)
e_Temp_Qty_6.grid(row=31, column=5)
e_Temp_Qty_6.config(font=entryfont)
cb_6_Press_Units: Combobox = Combobox(inside_frame, values=press_units, textvariable=eci_6_press_units, width=10)
cb_6_Press_Units.grid(row=31, column=6)
cb_6_Press_Units.config(font=entryfont)
cb_6_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Press_Qty_6 = Entry(inside_frame, text="", textvariable=eci_press_6_qty, width=8)
e_Press_Qty_6.grid(row=31, column=7)
e_Press_Qty_6.config(font=entryfont)

lbl_blank = Label(inside_frame, text="")
lbl_blank.grid(row=32, column=0)
lbl_blank.config(font=labelfont)

lbl_Equipment = Label(inside_frame, text="Equipment", width=10)
lbl_Equipment.grid(row=33, column=0)
lbl_Equipment.config(font=labelfont)
lbl_Energy_type = Label(inside_frame, text="Energy type", width=10)
lbl_Energy_type.grid(row=33, column=1) #, sticky=W)
lbl_Energy_type.config(font=labelfont)
lbl_Energy_amount = Label(inside_frame, text="Energy amount", width=12)
lbl_Energy_amount.grid(row=33, column=2) #, sticky=W)
lbl_Energy_amount.config(font=labelfont)
lbl_Catalyst = Label(inside_frame, text="Catalyst", width=10)
lbl_Catalyst.grid(row=33, column=3) #, sticky=W)
lbl_Catalyst.config(font=labelfont)
lbl_Side_effects = Label(inside_frame, text="Side effects", width=12)
lbl_Side_effects.grid(row=33, column=4)
lbl_Side_effects.config(font=labelfont)
lbl_By_products = Label(inside_frame, text="By-products", width=10)
lbl_By_products.grid(row=33, column=5) #, sticky=W)
lbl_By_products.config(font=labelfont)
lbl_Variables = Label(inside_frame, text="Variables")
lbl_Variables.grid(row=33, column=6) #, sticky=W)
lbl_Variables.config(font=labelfont)
lbl_Variables = Label(inside_frame, text="Values", width=10)
lbl_Variables.grid(row=33, column=7) #, sticky=W)
lbl_Variables.config(font=labelfont)

cb_Equipment: Combobox = Combobox(inside_frame, values=equipment, textvariable=equipment_selected, width=12)
cb_Equipment.grid(row=34, column=0)
cb_Equipment.config(font=entryfont)
cb_Energy_type: Combobox = Combobox(inside_frame, values=energy_type, textvariable=energy_type_selected, width=12)
cb_Energy_type.grid(row=34, column=1) #, sticky=W)
cb_Energy_type.config(font=entryfont)
e_Energy_amount = Entry(inside_frame, text="", textvariable=energy_amount, width=12)
e_Energy_amount.grid(row=34, column=2)
e_Energy_amount.config(font=entryfont)
cb_Catalyst: Combobox = Combobox(inside_frame, values=catalyst, textvariable=catalyst_selected, width=12)
cb_Catalyst.grid(row=34, column=3) #, sticky=W)
cb_Catalyst.config(font=entryfont)
cb_Side_effects: Combobox = Combobox(inside_frame, values=side_effects, textvariable=side_effect_selected, width=12)
cb_Side_effects.grid(row=34, column=4)
cb_Side_effects.config(font=entryfont)
cb_By_products: Combobox = Combobox(inside_frame, values=by_products, textvariable=by_product_selected, width=12)
cb_By_products.grid(row=34, column=5) #, sticky=W)
cb_By_products.config(font=entryfont)
cb_Variables: Combobox = Combobox(inside_frame, values=variables, textvariable=variable_selected, width=12)
cb_Variables.grid(row=34, column=6) #, sticky=W)
cb_Variables.config(font=entryfont)
e_Variable_Value = Entry(inside_frame, text="", textvariable=variable_value, width=8)
e_Variable_Value.grid(row=34, column=7)
e_Variable_Value.config(font=entryfont)

lbl_Explanation = Label(inside_frame, text="Explanation", width=10)
lbl_Explanation.grid(row=35, column=0)
lbl_Explanation.config(font=labelfont)
lbl_Explanation = Label(inside_frame, text="Super subscript ", width=12)
lbl_Explanation.grid(row=35, column=1)
lbl_Explanation.config(font=labelfont)
lbl_LU_Process = Label(inside_frame, text='360\u2070 \u2070C H\u2082O')  # C2H3O2-
lbl_LU_Process.grid(row=35, column=2)
lbl_LU_Process.config(font=labelfont)
'''
unicode numbers. degrees: \u2070 subscript 2: \u2082 subscript 3: \u2083 subscript e: \u2091
superscript 2:\u00B2 superscript 3:\u00B3 superscript 4: \u2074 superscript -: \u207B
'''
lbl_LU_Process = Label(inside_frame, text='X\u2074 + X\u00B2 = 0')
lbl_LU_Process.grid(row=35, column=3)
lbl_LU_Process.config(font=labelfont)
lbl_LU_Process = Label(inside_frame, text='C\u2082H\u2083O\u2082\u207B C\u2082H\u2083O\u00B2\u207B')
# lbl_LU_Process = Label(text='C\u00B2\u207A Fe\u00B3\u207A Cl\u207B e\u207B')
lbl_LU_Process.grid(row=35, column=4)
lbl_LU_Process.config(font=labelfont)
lbl_LU_Process = Label(inside_frame,text='Cl\u2091 Fe\u00B3\u207A ')
lbl_LU_Process.grid(row=35, column=5)
lbl_LU_Process.config(font=labelfont)
e_Explanation = Text(inside_frame, height=6, width=100)
e_Explanation.grid(row=36, column=0, columnspan=6) #, sticky=W)
e_Explanation.config(font=entryfont)
e_Explanation.rowconfigure(99)
lbl_blank = Label(inside_frame, text="")
lbl_blank.grid(row=40, column=0, columnspan=2)
lbl_blank.config(font=labelfont)
lbl_blank = Label(inside_frame, text="")
lbl_blank.grid(row=41, column=0, columnspan=2)
lbl_blank.config(font=labelfont)
lbl_blank = Label(inside_frame, text="")
lbl_blank.grid(row=42, column=0, columnspan=2)
lbl_blank.config(font=labelfont)

if __name__ == '__main__':
    root.mainloop()


