# https://leetcode.cn/contest/weekly-contest-403/
from check import check
from interpret_solution import interpret_solution,get_interpret_solution_data
from get_quesstion_id import get_question_id_by_name


java_code='''class Solution {
    public boolean robot(String command, int[][] obstacles, int x, int y) {
        //多次循环 找到模式
        //学到了新的存储坐标的方法  左坐标左移30 | 右坐标
        int xx=0,yy=0;
        Set<Long> ss=new HashSet<>();
        ss.add(((long)xx << 30) | yy);
        for(int i=0;i<command.length();i++){
            if(command.charAt(i)=='U'){
                yy++;
            }else{
                xx++;
            }
            ss.add(((long)xx << 30) | yy);
        }
        int cir=Math.min(x/xx,y/yy);
        if(ss.contains(((long)(x-cir*xx) << 30) | (y-cir*yy))==false){
            return false;
        }
        for(int[] s:obstacles){
            if(s.length!=2) continue;
             int x1=s[0];
            int y1=s[1];
            if(x1 >x || y1>y) continue;
           cir=Math.min(x1/xx,y1/yy);
        if(ss.contains(((long)(x1-cir*xx) << 30) | (y1-cir*yy))==true){
            return false;
        }
        }
        return true;
    }
}'''
# LCP 03. 机器人大冒险
# programmable-robot
# https://leetcode.cn/problems/programmable-robot
question_id=get_question_id_by_name("programmable-robot")
submit_data=get_interpret_solution_data(
    lang="java",
    question_id=question_id,
    typed_code=java_code,
    data_input="\"URR\"\n[]\n3\n2\n\"URR\"\n[[2, 2]]\n3\n2\n\"URR\"\n[[4, 2]]\n3\n2"
)

interpret_solution_result=interpret_solution(submit_data)
if interpret_solution_result is None:
    pass
else:
    interpret_id=interpret_solution_result["interpret_id"]

    check_result=check(interpret_id)
    print(check_result)