# Databricks notebook source
# MAGIC %run  /MyNoteBooks/test2notebook

# COMMAND ----------

print (full_name)

# COMMAND ----------

# MAGIC %fs

# COMMAND ----------

dbutil.help()

# COMMAND ----------

dbutils.help()

# COMMAND ----------




# COMMAND ----------

dbutils.fs.ls('/MyNoteBooks')

# COMMAND ----------

files =dbutils.fs.ls('/MyNoteBooks')
print (files)

# COMMAND ----------

display(dbutils.help())


# COMMAND ----------

# MAGIC %md
