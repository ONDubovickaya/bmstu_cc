; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = alloca [8 x i8]
  store [8 x i8] c"While:\0a\00", [8 x i8]* %".2"
  %".4" = getelementptr [8 x i8], [8 x i8]* %".2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  %".6" = alloca i32
  store i32 1, i32* %".6"
  br label %"entryloop_do"
entryloop_do:
  br label %"entry.loop_cond"
entry.loop_cond:
  %".10" = load i32, i32* %".6"
  %".11" = icmp slt i32 %".10", 30
  br i1 %".11", label %"entry.loop_body", label %"entry.loop_end"
entry.loop_body:
  %".13" = load i32, i32* %".6"
  %".14" = alloca [4 x i8]
  store [4 x i8] c"%d \00", [4 x i8]* %".14"
  %".16" = getelementptr [4 x i8], [4 x i8]* %".14", i32 0, i32 0
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i32 %".13")
  %".18" = load i32, i32* %".6"
  %".19" = mul i32 %".18", 3
  store i32 %".19", i32* %".6"
  br label %"entry.loop_update"
entry.loop_end:
  %".23" = alloca [2 x i8]
  store [2 x i8] c"\0a\00", [2 x i8]* %".23"
  %".25" = getelementptr [2 x i8], [2 x i8]* %".23", i32 0, i32 0
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".25")
  ret i32 0
entry.loop_update:
  br label %"entry.loop_cond"
}
