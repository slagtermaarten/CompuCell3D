
import os
import sys
from PyQt4.QtCore import QEvent, Qt
from PyQt4.QtGui import QApplication

class CQApplication(QApplication):
    def __init__(self, argv):
        """
        Constructor
        """
        QApplication.__init__(self, argv)
        self.__objectRegistry = {}
        self.__pluginObjectRegistry = {}
        
    def registerObject(self, name, object):
        """
        Public method to register an object in the object registry.
        
        @param name name of the object (string)
        @param object reference to the object
        @exception KeyError raised when the given name is already in use
        """
        if self.__objectRegistry.has_key(name):
            raise KeyError('Object "%s" already registered.' % name)
        else:
            self.__objectRegistry[name] = object
        
    def getObject(self, name):
        """
        Public method to get a reference to a registered object.
        
        @param name name of the object (string)
        @return reference to the registered object
        @exception KeyError raised when the given name is not known
        """
        if self.__objectRegistry.has_key(name):
            return self.__objectRegistry[name]
        else:
            raise KeyError('Object "%s" is not registered.' % name)
        
    def registerPluginObject(self, name, object):
        """
        Public method to register a plugin object in the object registry.
        
        @param name name of the plugin object (string)
        @param object reference to the plugin object
        @exception KeyError raised when the given name is already in use
        """
        if self.__pluginObjectRegistry.has_key(name):
            raise KeyError('Pluginobject "%s" already registered.' % name)
        else:
            self.__pluginObjectRegistry[name] = object
        
    def unregisterPluginObject(self, name):
        """
        Public method to unregister a plugin object in the object registry.
        
        @param name name of the plugin object (string)
        """
        if self.__pluginObjectRegistry.has_key(name):
            del self.__pluginObjectRegistry[name]
        
    def getPluginObject(self, name):
        """
        Public method to get a reference to a registered plugin object.
        
        @param name name of the plugin object (string)
        @return reference to the registered plugin object
        @exception KeyError raised when the given name is not known
        """
        if self.__pluginObjectRegistry.has_key(name):
            return self.__pluginObjectRegistry[name]
        else:
            raise KeyError('Pluginobject "%s" is not registered.' % name)
        
    def getPluginObjects(self):
        """
        Public method to get a list of (name, reference) pairs of all
        registered plugin objects.
        
        @return list of (name, reference) pairs
        """
        return self.__pluginObjectRegistry.items()
