; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define void @"char_array_test"()
{
entry:
  %".2" = trunc i32 33 to i8
  %".3" = alloca i8
  store i8 %".2", i8* %".3"
  %".5" = load i8, i8* %".3"
  %".6" = alloca [10 x i8]
  store [10 x i8] c"33 is %c\0a\00", [10 x i8]* %".6"
  %".8" = getelementptr [10 x i8], [10 x i8]* %".6", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i8 %".5")
  %".10" = alloca [12 x i8]
  store [12 x i8] c"Hello world\00", [12 x i8]* %".10"
  %".12" = getelementptr [12 x i8], [12 x i8]* %".10", i32 0, i32 0
  %".13" = alloca [4 x i8]
  store [4 x i8] c"%s\0a\00", [4 x i8]* %".13"
  %".15" = getelementptr [4 x i8], [4 x i8]* %".13", i32 0, i32 0
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i8* %".12")
  ret void
}

define i32 @"main"()
{
entry:
  %".2" = alloca [3 x [4 x i32]]
  store [3 x [4 x i32]] [[4 x i32] [i32 1, i32 2, i32 3, i32 4], [4 x i32] [i32 5, i32 6, i32 7, i32 8], [4 x i32] [i32 9, i32 11, i32 12, i32 13]], [3 x [4 x i32]]* %".2"
  %".4" = alloca [8 x i8]
  store [8 x i8] c"array=\0a\00", [8 x i8]* %".4"
  %".6" = getelementptr [8 x i8], [8 x i8]* %".4", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6")
  %".8" = alloca i32
  store i32 0, i32* %".8"
  br label %"entryloop_do"
entryloop_do:
  br label %"entry.loop_cond"
entry.loop_cond:
  %".12" = load i32, i32* %".8"
  %".13" = icmp slt i32 %".12", 3
  br i1 %".13", label %"entry.loop_body", label %"entry.loop_end"
entry.loop_body:
  %".15" = alloca i32
  store i32 0, i32* %".15"
  br label %"entry.loop_bodyloop_do"
entry.loop_end:
  call void @"char_array_test"()
  ret i32 0
entry.loop_update:
  %".43" = load i32, i32* %".8"
  %".44" = add i32 %".43", 1
  store i32 %".44", i32* %".8"
  br label %"entry.loop_cond"
entry.loop_bodyloop_do:
  br label %"entry.loop_body.loop_cond"
entry.loop_body.loop_cond:
  %".19" = load i32, i32* %".15"
  %".20" = icmp slt i32 %".19", 4
  br i1 %".20", label %"entry.loop_body.loop_body", label %"entry.loop_body.loop_end"
entry.loop_body.loop_body:
  %".22" = getelementptr [3 x [4 x i32]], [3 x [4 x i32]]* %".2", i32 0, i32 0
  %".23" = load i32, i32* %".8"
  %".24" = getelementptr [3 x [4 x i32]], [3 x [4 x i32]]* %".2", i32 0, i32 %".23"
  %".25" = load [4 x i32], [4 x i32]* %".24"
  %".26" = load i32, i32* %".15"
  %".27" = getelementptr [4 x i32], [4 x i32]* %".24", i32 0, i32 %".26"
  %".28" = load i32, i32* %".27"
  %".29" = alloca [4 x i8]
  store [4 x i8] c"%d\09\00", [4 x i8]* %".29"
  %".31" = getelementptr [4 x i8], [4 x i8]* %".29", i32 0, i32 0
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".31", i32 %".28")
  br label %"entry.loop_body.loop_update"
entry.loop_body.loop_end:
  %".38" = alloca [2 x i8]
  store [2 x i8] c"\0a\00", [2 x i8]* %".38"
  %".40" = getelementptr [2 x i8], [2 x i8]* %".38", i32 0, i32 0
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".40")
  br label %"entry.loop_update"
entry.loop_body.loop_update:
  %".34" = load i32, i32* %".15"
  %".35" = add i32 %".34", 1
  store i32 %".35", i32* %".15"
  br label %"entry.loop_body.loop_cond"
}
