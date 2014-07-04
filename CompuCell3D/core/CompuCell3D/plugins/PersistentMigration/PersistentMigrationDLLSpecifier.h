#ifndef PERSISTENTMIGRATION_EXPORT_H
#define PERSISTENTMIGRATION_EXPORT_H

    #if defined(_WIN32)
      #ifdef PersistentMigrationShared_EXPORTS
          #define PERSISTENTMIGRATION_EXPORT __declspec(dllexport)
          #define PERSISTENTMIGRATION_EXPIMP_TEMPLATE
      #else
          #define PERSISTENTMIGRATION_EXPORT __declspec(dllimport)
          #define PERSISTENTMIGRATION_EXPIMP_TEMPLATE extern
      #endif
    #else
         #define PERSISTENTMIGRATION_EXPORT
         #define PERSISTENTMIGRATION_EXPIMP_TEMPLATE
    #endif

#endif
