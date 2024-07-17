; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = alloca [6 x i32]
  store [6 x i32] [i32 4, i32 5, i32 6, i32 7, i32 8, i32 9], [6 x i32]* %".2"
  %".4" = alloca i32
  store i32 0, i32* %".4"
  %".6" = alloca i32
  store i32 0, i32* %".6"
  br label %"entryloop_do"
entryloop_do:
  br label %"entry.loop_cond"
entry.loop_cond:
  %".10" = load i32, i32* %".6"
  %".11" = icmp slt i32 %".10", 6
  br i1 %".11", label %"entry.loop_body", label %"entry.loop_end"
entry.loop_body:
  %".13" = getelementptr [6 x i32], [6 x i32]* %".2", i32 0, i32 0
  %".14" = load i32, i32* %".6"
  %".15" = getelementptr [6 x i32], [6 x i32]* %".2", i32 0, i32 %".14"
  %".16" = load i32, i32* %".15"
  %".17" = alloca [4 x i8]
  store [4 x i8] c"%d\09\00", [4 x i8]* %".17"
  %".19" = getelementptr [4 x i8], [4 x i8]* %".17", i32 0, i32 0
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", i32 %".16")
  %".21" = load i32, i32* %".4"
  %".22" = getelementptr [6 x i32], [6 x i32]* %".2", i32 0, i32 0
  %".23" = load i32, i32* %".6"
  %".24" = getelementptr [6 x i32], [6 x i32]* %".2", i32 0, i32 %".23"
  %".25" = load i32, i32* %".24"
  %".26" = add i32 %".21", %".25"
  store i32 %".26", i32* %".4"
  br label %"entry.loop_update"
entry.loop_end:
  %".33" = load i32, i32* %".4"
  %".34" = alloca [11 x i8]
  store [11 x i8] c"\0asum = %d\0a\00", [11 x i8]* %".34"
  %".36" = getelementptr [11 x i8], [11 x i8]* %".34", i32 0, i32 0
  %".37" = call i32 (i8*, ...) @"printf"(i8* %".36", i32 %".33")
  ret i32 0
entry.loop_update:
  %".29" = load i32, i32* %".6"
  %".30" = add i32 %".29", 1
  store i32 %".30", i32* %".6"
  br label %"entry.loop_cond"
}
