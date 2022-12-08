# saveload-test


## TEST CASE 1

测试自定义的类，保存之后，在另一个项目中导入

### STEPS
```shell
# create virtual env and activate
conda create -n "test_case_1" python=3.9
conda activate test_case_1
# install requirements
pip install joblib
# execute script
cd test_case_1
cd save
python main.py
cd ../load
python main.py
```

### RESULT **[FAILED]**
```python
Traceback (most recent call last):
  File "D:\Documents\Git\SELF_UNS_PROJECTS\saveload-test\test_case_1\load\main.py", line 3, in <module>
    mouse = joblib.load('../mouse.pkl')
  File "D:\Anaconda3\lib\site-packages\joblib\numpy_pickle.py", line 587, in load
    obj = _unpickle(fobj, filename, mmap_mode)
  File "D:\Anaconda3\lib\site-packages\joblib\numpy_pickle.py", line 506, in _unpickle
    obj = unpickler.load()
  File "D:\Anaconda3\lib\pickle.py", line 1212, in load
    dispatch[key[0]](self)
  File "D:\Anaconda3\lib\pickle.py", line 1537, in load_stack_global
    self.append(self.find_class(module, name))
  File "D:\Anaconda3\lib\pickle.py", line 1579, in find_class
    __import__(module, level=0)
ModuleNotFoundError: No module named 'klass'
```

## TEST CASE 2

测试项目中引入第三方库，保存之后，在另一个项目中导入

### STEPS
```shell
# create virtual env and activate
conda create -n "test_case_2" python=3.9
conda activate test_case_2
# install requirements
pip install joblib torch
# execute script
cd test_case_2
cd save
python main.py
cd ../load
# change to env "test_case_1" (no torch module)
python main.py
```

### RESULT **[FAILED]**
```python
Traceback (most recent call last):
  File ".\main.py", line 3, in <module>
    t = joblib.load('../tensor.pkl')
  File "D:\Anaconda3\envs\labelme\lib\site-packages\joblib\numpy_pickle.py", line 587, in load
    obj = _unpickle(fobj, filename, mmap_mode)
  File "D:\Anaconda3\envs\labelme\lib\site-packages\joblib\numpy_pickle.py", line 506, in _unpickle
    obj = unpickler.load()
  File "D:\Anaconda3\envs\labelme\lib\pickle.py", line 1050, in load
    dispatch[key[0]](self)
  File "D:\Anaconda3\envs\labelme\lib\pickle.py", line 1347, in load_stack_global
    self.append(self.find_class(module, name))
  File "D:\Anaconda3\envs\labelme\lib\pickle.py", line 1388, in find_class
    __import__(module, level=0)
ModuleNotFoundError: No module named 'torch'
```