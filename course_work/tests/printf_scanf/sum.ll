; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"scanf"(i8* %".1", ...)

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = alloca [37 x i8]
  store [37 x i8] c"Please input number a (int values): \00", [37 x i8]* %".2"
  %".4" = getelementptr [37 x i8], [37 x i8]* %".2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  %".6" = alloca i32
  %".7" = alloca i32
  store i32 2, i32* %".7"
  %".9" = load i32, i32* %".6"
  %".10" = alloca [3 x i8]
  store [3 x i8] c"%d\00", [3 x i8]* %".10"
  %".12" = getelementptr [3 x i8], [3 x i8]* %".10", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"scanf"(i8* %".12", i32* %".6")
  %".14" = load i32, i32* %".7"
  %".15" = load i32, i32* %".6"
  %".16" = add i32 %".15", %".14"
  %".17" = alloca [12 x i8]
  store [12 x i8] c"a + c = %d\0a\00", [12 x i8]* %".17"
  %".19" = getelementptr [12 x i8], [12 x i8]* %".17", i32 0, i32 0
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", i32 %".16")
  ret i32 0
}
