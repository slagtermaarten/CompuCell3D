
#ifndef BIONETWORKSBML_H
#define BIONETWORKSBML_H

#include <iostream>
#include "BionetworkDLLSpecifier.h"
class soslib_OdeModel;
class soslib_CvodeSettings;

class BIONETWORK_EXPORT BionetworkSBML {
    private:
        std::string modelName;
        std::string modelKey;
        std::string fileName;
        double timeStepSize;
        soslib_OdeModel * odeModel;
        soslib_CvodeSettings * settings;
    public:
        BionetworkSBML(std::string);
        BionetworkSBML(std::string, std::string);
        BionetworkSBML(std::string, std::string, double);
        ~BionetworkSBML();
        
        void setModelKey(std::string key){ modelKey = key; };
        std::string getModelKey() const { return modelKey; };
        void setModelName(std::string name){ modelName = name; };
        std::string getModelName() const { return modelName; };
        
		std::string getModelPath() const { return fileName; };

        const soslib_OdeModel * getOdeModel() const {return odeModel;};
        const soslib_CvodeSettings * getSettings() const {return settings;};
        
        double getTimeStepSize() const { return timeStepSize; };
        
        bool hasVariable(std::string) const ;
        
        void printSBMLModelInfo();
};


#endif





