import pickle;

#使用pickle模块将数据对象保存到文件
data1 = {"a":[1,2.0,3,4+6j],
         "b":("string",u"Unicode string"),
         "c":None};

selfref_list = [1,2,3];
selfref_list.append(selfref_list);
#print(selfref_list);

output = open("data.pkl","wb");

#pickle dictionary using protocol 0
pickle.dump(data1,output);
#pickle the list using the highest protocol variable
pickle.dump(selfref_list,output);

output.close();

