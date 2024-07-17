; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

%"Student" = type {i32, double}
declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = alloca %"Student"
  %".3" = getelementptr %"Student", %"Student"* %".2", i32 0, i32 0
  %".4" = getelementptr %"Student", %"Student"* %".2", i32 0, i32 0
  %".5" = load i32, i32* %".4"
  store i32 20, i32* %".4"
  %".7" = getelementptr %"Student", %"Student"* %".2", i32 0, i32 0
  %".8" = getelementptr %"Student", %"Student"* %".2", i32 0, i32 1
  %".9" = load double, double* %".8"
  store double 0x4012000000000000, double* %".8"
  %".11" = getelementptr %"Student", %"Student"* %".2", i32 0, i32 0
  %".12" = getelementptr %"Student", %"Student"* %".2", i32 0, i32 0
  %".13" = load i32, i32* %".12"
  %".14" = alloca [17 x i8]
  store [17 x i8] c"Student age: %d\0a\00", [17 x i8]* %".14"
  %".16" = getelementptr [17 x i8], [17 x i8]* %".14", i32 0, i32 0
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i32 %".13")
  %".18" = getelementptr %"Student", %"Student"* %".2", i32 0, i32 0
  %".19" = getelementptr %"Student", %"Student"* %".2", i32 0, i32 1
  %".20" = load double, double* %".19"
  %".21" = alloca [18 x i8]
  store [18 x i8] c"Student GPA: %.2f\00", [18 x i8]* %".21"
  %".23" = getelementptr [18 x i8], [18 x i8]* %".21", i32 0, i32 0
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23", double %".20")
  ret i32 0
}
