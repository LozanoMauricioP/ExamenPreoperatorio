# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 12:24:34 2018

@author: Mauricio Perez Lozano
"""

##librerias

import sys 
from PyQt5.QtWidgets import QApplication,QDialog, QButtonGroup
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtCore
import smtplib
from email.mime.text import MIMEText

##Esta clase permite ingresar y capturar en cada uno de los datos de un paciente
class Paciente(object):
##Atributos de la clase paciente
    def __init__(self,nombre,cedula,sexo,sangre,edad,estatura,peso):
        self.__nombre=nombre
        self.__cedula=cedula
        self.__edad=edad
        self.__sangre=sexo
        self.__sexo=sexo
        self.__estatura=estatura
        self.__peso=peso
        self.__enfcp = False
        self.__enfcv = False
        self.__anemia = False
        self.__hemostasia = False
        self.__tratac = False
        self.__polifagia = False
        self.__glucosa = False
        self.__diabetes = False
        self.__renales = False
        self.__actsex = False
        self.__iq = False

##Metodos set y get         
    def setNombre(self,n):
        self.__nombre = n;   
    def getNombre(self):
        return self.__nombre;
    
    def setCedula(self,c):
        self.__cedula = c;
        self.__cedula = c;
    def getCedula(self):
        return self.__cedula;
    
    def setSexo(self,g):
        self.__sexo = g;   
    def getSexo(self):
        return self.__sexo;
    def setEdad(self,edad):
        self.__edad=edad
    def getEdad(self):
        return self.__edad
    def setPeso(self,p):
        self.__peso=p
    def getPeso(self):
        return self.__peso
    def setEstatura(self,e):
        self.__estatura=e
    def getEstatura(self):
        return self.__estatura
    
    def setEnfcp(self,ecp):
        self.__enfcp=ecp
    def getEnfcp(self):
        return self.__enfcp
    def setEnfcv(self,ecv):
        self.__enfcv=ecv
    def getEnfcv(self):
        return self.__enfcv
    def setAnemia(self,ane):
        self.__anemia=ane
    def getAnemia(self):
        return self.__anemia
    def setHemostasia(self,hemo):
        self.__hemostasia=hemo
    def getHemostasia(self):
        return self.__hemostasia
    def setTratac(self,trat):
        self.__hemostasia=trat
    def getTratac(self):
        return self.__tratac
    def setPolifagia(self,poli):
        self.__polifagia=poli
    def getPolifagia(self):
        return self.__polifagia
    def setGlucosa(self,glu):
        self.__glucosa=glu
    def getGlucosa(self):
        return self.__glucosa
    def setDiabetes(self,diab):
        self.__diabetes=diab
    def getDiabetes(self):
        return self.__diabetes
    def setRenales(self,rena):
        self.__renales=rena
    def getRenales(self):
        return self.__renales
    def setActsex(self,act):
        self.__actsex=act
    def getActsex(self):
        return self.__actsex
    def setIq(self,iq):
        self.__iq=iq
    def getIq(self):
        return self.__iq
#Esta clase permite ingresar el nombre, cedula y accerder a la lista de los pacientes a un medico    
class Medico(object):
##Atributos de la clase Medico
    def __init__(self,nombre,cedula): 
        self.__nombre = nombre; 
        self.__cedula = cedula; 
        self.__lista_pacientes = {} 
##Metodos set y get    
    def setNombre(self,n):
        self.__nombre = n;   
    def getNombre(self):
        return self.__nombre;
    
    def setCedula(self,c):
        self.__cedula = c;
    def getCedula(self):
        return self.__cedula;
 #metodo para acceder a un paciente a la lista_pacientes  
    def getPaciente(self,cedula):
        paciente = self.__lista_pacientes[cedula]
        return paciente
#metodo para verificar si un paciente ya esta en la lista_pacientes   
    def existePaciente(self,cedula):
        if cedula in self.__lista_pacientes:
            return True
        return False
#metodo para ingresar  un paciente a la lista_pacientes    
    def ingresarPaciente(self,paciente):
        cedula = paciente.getCedula();
        e = self.existePaciente(cedula);
        if e == True:
            return "El paciente ya existe"
        #se genera el paciente nuevo: un objeto de la clase Paciente
        #se anade a la lista
        self.__lista_pacientes[cedula] = paciente;
        return "Paciente ingresado correctamente";
    
m = Medico('Juan',123)

##Clases para visualizar e ingresar un paciente en una de las ventanas

class IngresarPaciente(QDialog):
    def __init__(self, parent=None):
        super(IngresarPaciente,self).__init__(parent)
        loadUi('registroPaciente.ui',self)
        self.group()
        regex= QtCore.QRegExp("[a-z-A-Z-_ _]+")
        self.nombre_text.setValidator(QtGui.QRegExpValidator(regex))
        self.documento_text.setValidator(QtGui.QIntValidator());
        self.edad_text.setValidator(QtGui.QIntValidator());
        self.estatura_text.setValidator(QtGui.QIntValidator());
        self.peso_text.setValidator(QtGui.QIntValidator());
        self.guardar.clicked.connect(self.guardarPaciente)
##Metodo para ingresar el paciente        
    def guardarPaciente(self):
        cadena,cadena2,validar = self.validarIngreso()
        if validar:
            cedula = int(self.documento_text.text())
            if m.existePaciente(cedula):
                cadena = 'El paciente ya existe.'
                self.confirmar.setText(cadena)
            else:
                nombre = self.nombre_text.text()
                if self.femenino.isChecked():
                    sexo = 'Femenino'
                else:
                    sexo = 'Masculino'
                if self.radioA.isChecked():
                    sangre = 'A+'
                elif self.radioA2.isChecked():
                    sangre = 'A-'
                elif self.radioAB.isChecked():
                    sangre = 'AB+'
                elif self.radioAB2.isChecked():
                    sangre = 'AB-'
                elif self.radioB.isChecked():
                    sangre = 'B+'
                elif self.radioB2.isChecked():
                    sangre = 'B-'
                elif self.radioO.isChecked():
                    sangre = 'O+'
                else:
                    sangre = 'O-'
                edad = int(self.edad_text.text())
                estatura = int(self.estatura_text.text())
                peso = int(self.peso_text.text())
                paciente = Paciente(nombre,cedula,sexo,sangre,edad,estatura,peso)
                cadena = m.ingresarPaciente(paciente)
                self.reset()
                self.confirmar.setText(cadena)
        else:
            if cadena2 == 'Datos incorrectos: ':
                self.confirmar.setText(cadena)
            else:
                if cadena == 'Se deben llenar los campos:':
                    self.confirmar.setText(cadena2)
                else:
                    self.confirmar.setText(cadena+'\n'+cadena2)
##Metodos para validar          
    def validarIngreso(self):
        cadena = 'Se deben llenar los campos:'
        cadena2 = 'Datos incorrectos: '
        cont = 0
        if self.nombre_text.text() == '':
            cont+=1
            cadena+= ' - Nombre'
        if self.documento_text.text() == '':
            cont+=1
            cadena+= ' - Documento'
        elif int(self.documento_text.text())<=0:
            cont+=1
            cadena2+= ' - Documento'
            
        if self.edad_text.text() == '':
            cont+=1
            cadena+= ' - Edad'
        elif int(self.edad_text.text())<0 or int(self.edad_text.text())>200:
            cont+=1
            cadena2+= ' - Edad'
            
        if self.estatura_text.text() == '':
            cont+=1
            cadena+= ' - Estatura'
        elif int(self.estatura_text.text())<0 or int(self.estatura_text.text())>300:
            cont+=1
            cadena2+= ' - Estatura'
            
        if self.peso_text.text() == '':
            cont+=1
            cadena+= ' - Peso'
        elif int(self.peso_text.text())<0 or int(self.peso_text.text())>800:
            cont+=1
            cadena2+= ' - Peso'
            
        if self.sangreisnotCheck():
            cont+=1
            cadena+= ' - Tipo de Sangre' 
        if self.sexoisnotCheck():
            cont+=1
            cadena+= ' - Sexo'
        if cont == 0:
            return cadena,cadena2,True
        else:
            return cadena,cadena2,False

    def sexoisnotCheck(self):
        if self.femenino.isChecked():
            return False
        if self.masculino.isChecked():
            return False
        return True
    
    def sangreisnotCheck(self):
        if self.radioA.isChecked():
            return False
        if self.radioA2.isChecked():
            return False
        if self.radioAB.isChecked():
            return False
        if self.radioAB2.isChecked():
            return False
        if self.radioB.isChecked():
            return False
        if self.radioB2.isChecked():
            return False
        if self.radioO.isChecked():
            return False
        if self.radioO2.isChecked():
            return False
        return True
##Metodos para resetear el sistema
    def reset(self):
        
        self.nombre_text.setText('')
        self.documento_text.setText('') 
        self.estatura_text.setText('') 
        self.edad_text.setText('') 
        self.peso_text.setText('') 
        
        self.group.setExclusive(False)        
        self.radioA.setChecked(False)
        self.radioA2.setChecked(False)
        self.radioAB.setChecked(False)
        self.radioAB2.setChecked(False)
        self.radioB.setChecked(False)
        self.radioB2.setChecked(False)
        self.radioO.setChecked(False)
        self.radioO2.setChecked(False)
        self.group.setExclusive(True)
        
        self.group2.setExclusive(False)   
        self.femenino.setChecked(False)
        self.masculino.setChecked(False)
        self.group2.setExclusive(True)
##        
    def group(self):
        self.group = QButtonGroup()      
        self.group.addButton(self.radioA)
        self.group.addButton(self.radioA2)    
        self.group.addButton(self.radioAB) 
        self.group.addButton(self.radioAB2) 
        self.group.addButton(self.radioB) 
        self.group.addButton(self.radioB2) 
        self.group.addButton(self.radioO) 
        self.group.addButton(self.radioO2)
        
        self.group2 = QButtonGroup()
        self.group2.addButton(self.femenino)
        self.group2.addButton(self.masculino)
##Clases para visaulizar e ingresar los antecedentes de un paciente mediante la ventana        
class EstablecerAntecedentes(QDialog):
    def __init__(self,parent=None):
        super(EstablecerAntecedentes,self).__init__(parent)
        loadUi('ventana_antecedentes.ui',self)  
        print(str(ced_temp))
        self.guardar.clicked.connect(self.guardarAntecedentes)
        self.salir.clicked.connect(self.salirA)
##Metodo para ingresar el paciente       
    def guardarAntecedentes(self):
        if self.validarAntecedentes():
            cadena = 'Antecedentes del paciente registrados.'
            paciente = m.getPaciente(ced_temp)
            if self.enfcp.isChecked():
                paciente.setEnfcp(True)
            if self.enfcv.isChecked():
                paciente.setEnfcv(True)
            if self.anemia.isChecked():
                paciente.setAnemia(True)
            if self.hemostasia.isChecked():
                paciente.setHemostasia(True)
            if self.tratac.isChecked():
                paciente.setTratac(True)
            if self.polifagia.isChecked():
                paciente.setPolifagia(True)
            if self.glucosa.isChecked():
                paciente.setGlucosa(True)
            if self.diabetes.isChecked():
                paciente.setDiabetes(True)
            if self.renales.isChecked():
                paciente.setRenales(True)
            if self.actsex.isChecked():
                paciente.setActsex(True)
            if self.iq.isChecked():
                paciente.setIq(True)
            self.confirmar.setText(cadena)
        else:
            cadena = 'Se deben llenar todos los campos.'
            self.confirmar.setText(cadena)
##Metodo para salir de la ventana antecedentes           
    def salirA(self):
        self.close();
##Metodo para validar los antecedentes    
    def validarAntecedentes(self):
        cont = 0
        
        if not self.enfcv.isChecked():
            if not self.enfcv_2.isChecked():
                cont+=1
            
        if not self.anemia.isChecked():
            if not self.anemia_2.isChecked():
                cont+=1        
            
        if not self.hemostasia.isChecked():
            if not self.hemostasia_2.isChecked():
                cont+=1
            
        if not self.tratac.isChecked():
            if not self.tratac_2.isChecked():
                cont+=1
            
        if not self.polifagia.isChecked():
            if not self.polifagia_2.isChecked():
                cont+=1
            
        if not self.glucosa.isChecked():
            if not self.glucosa_2.isChecked():
                cont+=1
            
        if not self.diabetes.isChecked():
            if not self.diabetes_2.isChecked():
                cont+=1
            
        if not self.renales.isChecked():
            if not self.renales_2.isChecked():
                cont+=1
            
        if not self.actsex.isChecked():
            if not self.actsex_2.isChecked():
                cont+=1
            
        if not self.iq.isChecked():
            if not self.iq_2.isChecked():
                cont+=1
            
        if cont==0:
            return True
        else:
            return False  
##Clase para  visualizar y llenar el formulario de los antecedentes     
class Formulario(QDialog):
    def __init__(self, parent=None):
        super(Formulario,self).__init__(parent)
        loadUi('ventana_validar.ui',self)
        self.validar.clicked.connect(self.formulario)
        self.documento_text.setValidator(QtGui.QIntValidator());
##Metodo para llenar el formulario       
    def formulario(self):
        cadena = self.validarDocumento();
        if cadena == '':
            global ced_temp##variable necesaria para traer datos desde una clase a otra
            ced_temp = int(self.documento_text.text())
            ventana = EstablecerAntecedentes(self)
            ventana.show()
            self.close()
        else:
            self.confirmar.setText(cadena)
##Metodo para validar el documento            
    def validarDocumento(self):    
        cadena = ''
        if self.documento_text.text() == '':
            cadena = 'Se debe ingresar el documento del paciente'   
            return cadena          
        elif int(self.documento_text.text())<0:
            cadena = 'Se ha ingresado un valor incorrecto'
            return cadena
        if m.existePaciente(int(self.documento_text.text())):
            return cadena
        else:
            cadena = 'No existe paciente con el documento de identidad indicado'
            return cadena
##Clase para visualizar e ingresar los examenes
class RegistrarExamenes(QDialog):
    def __init__(self,parent=None):
        super(RegistrarExamenes,self).__init__(parent)
        loadUi('ventana_examenes.ui',self)
        paciente = m.getPaciente(ced_temp)
        self.__cedula = paciente.getCedula()
        self.__nombre = paciente.getNombre()
        self.enviar.clicked.connect(self.enviarAntecedentes)
        self.salir.clicked.connect(self.salirE)
        #Validando
        sexo = paciente.getSexo()
        edad = paciente.getEdad()
        enfcp = paciente.getEnfcp()
        enfcv = paciente.getEnfcv()
        anemia = paciente.getAnemia()
        hemostasia = paciente.getHemostasia()
        tratac = paciente.getTratac()
        polifagia = paciente.getPolifagia()
        glucosa = paciente.getGlucosa()
        diabetes = paciente.getDiabetes()
        renales = paciente.getRenales()
        actsex = paciente.getActsex()
        iq = paciente.getIq()
        
        #Radiografia de Torax
        if enfcp == False:
            self.rd_text.setEnabled(False)
        #Electrocardiograma 
        if enfcv == False and iq ==False:
            self.ecg_text.setEnabled(False)
        #HEMATOCRITO
        if anemia == False:
            self.hcto_text.setEnabled(False)
        #PLAQUETA
        if hemostasia == False and tratac == False:
            self.rcp_text.setEnabled(False)
        #Glucosa
        if glucosa == False and diabetes ==False and polifagia==False:
            self.gs_text.setEnabled(False)
        #Nitrogeno ureico
        if renales == False and edad<65:
            self.renal_text.setEnabled(False)
        #PRUEBA DE EMBARAZO
        if sexo == 'Masculino':
            self.test_text.setEnabled(False)
        else:
            if actsex == False and edad<41:
                self.test_text.setEnabled(False)
##Metodo oara enviar los antecedentes    
    def enviarAntecedentes(self):
        if self.validar():
            mensaje = 'Dirigido a: Clinica Las Américas';
            mensaje += '\nDoctor: Luis Fernando Montoya :v'
            mensaje += '\n\nDesde el sistema de exámenes preoperatorios'
            mensaje += ' se acaba de registrar un paciente para su respectiva valoración.\n\n';
            
            mensaje += 'Documento de identidad: '+str(self.__cedula)
            mensaje += '\nNombre: '+self.__nombre
            
            rd = self.rd_text.text()
            if rd=='':
                mensaje += '\nRadiografía de Tórax: No aplica'
            else:
                mensaje += '\nRadiografía de Tórax: '+rd
                
            ecg = self.ecg_text.text()
            if ecg=='':
                mensaje += '\nElectrocardiograma: No aplica'
            else:
                mensaje += '\nElectrocardiograma: '+ecg
                
            hcto = self.hcto_text.text()
            if hcto=='':
                mensaje += '\nHematocrito/Hemaglobina: No aplica'
            else:
                mensaje += '\nHematocrito/Hemaglobina: '+hcto
                
            rcp = self.rcp_text.text()
            if rcp=='':
                mensaje += '\nRecuento de plaquetas: No aplica'
            else:
                mensaje += '\nRecuento de plaquetas: '+rcp
            
            gs = self.gs_text.text()
            if gs=='':
                mensaje += '\nGlucosa Sanguinea: No aplica'
            else:
                mensaje += '\nGlucosa Sanguinea: '+gs
                
            renal = self.test_text.text()
            if rd=='':
                mensaje += '\nNitrógeno uréico/Creatinina: No aplica'
            else:
                mensaje += '\nNitrógeno uréico/Creatinina: '+renal
            self.enviarCorreo(mensaje)
            self.confirmar.setText('Información enviada')
        else:
            self.confirmar.setText('Debe diligenciar todos los resultados')
##Metodo para validar   
    def validar(self):
        cont=0
        if self.rd_text.isEnabled():
            if self.rd_text.text()=='':
                cont+=1
            
        if self.ecg_text.isEnabled():
            if self.ecg_text.text()=='':
                cont+=1
            
        if self.hcto_text.isEnabled():
            if self.hcto_text.text()=='':
                cont+=1
            
        if self.rcp_text.isEnabled():
            if self.rcp_text.text()=='':
                cont+=1
        
        if self.gs_text.isEnabled():
            if self.gs_text.text()=='':
                cont+=1
            
        if self.renal_text.isEnabled():
            if self.renal_text.text()=='':
                cont+=1
        
        if self.test_text.isEnabled():
            if self.test_text.text()=='':
                cont+=1
        
        if cont==0:
            return True
        else:
            return False
##Metodo para enviar correo       
    def enviarCorreo(self,mensaje):    
        from_addr = 'examenes.preoperatorios@gmail.com'
        to = 'examenes.preoperatorios@gmail.com' # Correo del destinatario
        mime_message = MIMEText(mensaje, "plain")
        mime_message["From"] = from_addr
        mime_message["To"] = to
        mime_message["Subject"] = "Resultados de exámenes preoperatorios"
        # Reemplaza estos valores con tus credenciales de Google Mail
        username = 'examenes.preoperatorios@gmail.com'
        password = 'miexamen123'
        
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(from_addr, to, mime_message.as_string())     
        server.quit()
##Metodo para salir de la ventana    
    def salirE(self):
        self.close();


class Formulario2(QDialog):
    def __init__(self, parent=None):
        super(Formulario2,self).__init__(parent)
        loadUi('ventana_validar.ui',self)
        self.validar.clicked.connect(self.formulario)
        self.documento_text.setValidator(QtGui.QIntValidator());
        
    def formulario(self):
        cadena = self.validarDocumento();
        if cadena == '':
            global ced_temp ##variable necesaria para traer datos desde una clase a otra
            ced_temp = int(self.documento_text.text())
            ventana = RegistrarExamenes(self)
            ventana.show()
            self.close()
        else:
            self.confirmar.setText(cadena)
            
    def validarDocumento(self):    
        cadena = ''
        if self.documento_text.text() == '':
            cadena = 'Se debe ingresar el documento del paciente'   
            return cadena          
        elif int(self.documento_text.text())<0:
            cadena = 'Se ha ingresado un valor incorrecto'
            return cadena
        if m.existePaciente(int(self.documento_text.text())):
            return cadena
        else:
            cadena = 'No existe paciente con el documento de identidad indicado'
            return cadena
## clase para visualizar la ventana principal del sistema de cirugia        
class Sistema(QDialog):
    def __init__(self):
        self.lista_pacientes = {};
        super(Sistema,self).__init__()
        loadUi('ventana_principal.ui',self)
        self.ingresarPaciente.clicked.connect(self.ingresar_paciente)
        self.establecerAntecedentes.clicked.connect(self.establecer_Antecedentes)
        self.registrarExamenes.clicked.connect(self.registrar_Examenes)
        self.salir.clicked.connect(self.salirF)
##Metodos para visualizar las ventanas        
    def establecer_Antecedentes(self):
        ventana = Formulario(self)
        ventana.show()               
    
    def ingresar_paciente(self):
        ventana = IngresarPaciente(self)
        ventana.show()
    
    def registrar_Examenes(self):
        ventana = Formulario2(self)
        ventana.show() 
    
    def salirF(self):
        self.close()
       
app=QApplication(sys.argv)
widget=Sistema()
widget.show()
sys.exit(app.exec_())