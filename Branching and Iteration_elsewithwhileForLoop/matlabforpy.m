% % code1 ["for val in range(10):""print(val)" ];
% output = pyrun("pyformatlab.py");
% disp(output)
clc
% clear all
close all;
% pyrun("import pyformatlab");
out = pyrunfile("pyformatlab.py","evenValues");