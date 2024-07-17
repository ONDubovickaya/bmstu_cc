; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define void @"array_print"(i32* %".1", i32 %".2")
{
entry:
  %".4" = alloca [8 x i8]
  store [8 x i8] c"array=[\00", [8 x i8]* %".4"
  %".6" = getelementptr [8 x i8], [8 x i8]* %".4", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6")
  %".8" = alloca i32
  store i32 0, i32* %".8"
  br label %"entryloop_do"
entryloop_do:
  br label %"entry.loop_cond"
entry.loop_cond:
  %".12" = load i32, i32* %".8"
  %".13" = icmp slt i32 %".12", %".2"
  br i1 %".13", label %"entry.loop_body", label %"entry.loop_end"
entry.loop_body:
  %".15" = load i32, i32* %".8"
  %".16" = getelementptr i32, i32* %".1", i32 %".15"
  %".17" = load i32, i32* %".16"
  %".18" = alloca [5 x i8]
  store [5 x i8] c" %d \00", [5 x i8]* %".18"
  %".20" = getelementptr [5 x i8], [5 x i8]* %".18", i32 0, i32 0
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %".17")
  br label %"entry.loop_update"
entry.loop_end:
  %".27" = alloca [33 x i8]
  store [33 x i8] c"] and n=%d (number of elements)\0a\00", [33 x i8]* %".27"
  %".29" = getelementptr [33 x i8], [33 x i8]* %".27", i32 0, i32 0
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29", i32 %".2")
  ret void
entry.loop_update:
  %".23" = load i32, i32* %".8"
  %".24" = add i32 %".23", 1
  store i32 %".24", i32* %".8"
  br label %"entry.loop_cond"
}

define i32 @"main"()
{
entry:
  %".2" = alloca [7 x i32]
  store [7 x i32] [i32 3, i32 4, i32 5, i32 1, i32 0, i32 8, i32 9], [7 x i32]* %".2"
  %".4" = getelementptr [7 x i32], [7 x i32]* %".2", i32 0, i32 0
  call void @"array_print"(i32* %".4", i32 7)
  ret i32 0
}
