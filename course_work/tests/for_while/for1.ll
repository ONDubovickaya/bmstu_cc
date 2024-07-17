; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = alloca [28 x i8]
  store [28 x i8] c"Simple For (with massive):\0a\00", [28 x i8]* %".2"
  %".4" = getelementptr [28 x i8], [28 x i8]* %".2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  %".6" = alloca [6 x i32]
  store [6 x i32] [i32 4, i32 5, i32 6, i32 7, i32 8, i32 9], [6 x i32]* %".6"
  %".8" = alloca [7 x i8]
  store [7 x i8] c"data: \00", [7 x i8]* %".8"
  %".10" = getelementptr [7 x i8], [7 x i8]* %".8", i32 0, i32 0
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10")
  %".12" = alloca i32
  store i32 0, i32* %".12"
  br label %"entryloop_do"
entryloop_do:
  br label %"entry.loop_cond"
entry.loop_cond:
  %".16" = load i32, i32* %".12"
  %".17" = icmp slt i32 %".16", 6
  br i1 %".17", label %"entry.loop_body", label %"entry.loop_end"
entry.loop_body:
  %".19" = getelementptr [6 x i32], [6 x i32]* %".6", i32 0, i32 0
  %".20" = load i32, i32* %".12"
  %".21" = getelementptr [6 x i32], [6 x i32]* %".6", i32 0, i32 %".20"
  %".22" = load i32, i32* %".21"
  %".23" = alloca [5 x i8]
  store [5 x i8] c"%d, \00", [5 x i8]* %".23"
  %".25" = getelementptr [5 x i8], [5 x i8]* %".23", i32 0, i32 0
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".25", i32 %".22")
  br label %"entry.loop_update"
entry.loop_end:
  %".32" = alloca i32
  store i32 0, i32* %".32"
  %".34" = alloca i32
  store i32 0, i32* %".34"
  br label %"entry.loop_endloop_do"
entry.loop_update:
  %".28" = load i32, i32* %".12"
  %".29" = add i32 %".28", 1
  store i32 %".29", i32* %".12"
  br label %"entry.loop_cond"
entry.loop_endloop_do:
  br label %"entry.loop_end.loop_cond"
entry.loop_end.loop_cond:
  %".38" = load i32, i32* %".34"
  %".39" = icmp slt i32 %".38", 6
  br i1 %".39", label %"entry.loop_end.loop_body", label %"entry.loop_end.loop_end"
entry.loop_end.loop_body:
  %".41" = load i32, i32* %".32"
  %".42" = getelementptr [6 x i32], [6 x i32]* %".6", i32 0, i32 0
  %".43" = load i32, i32* %".34"
  %".44" = getelementptr [6 x i32], [6 x i32]* %".6", i32 0, i32 %".43"
  %".45" = load i32, i32* %".44"
  %".46" = add i32 %".41", %".45"
  store i32 %".46", i32* %".32"
  br label %"entry.loop_end.loop_update"
entry.loop_end.loop_end:
  %".53" = load i32, i32* %".32"
  %".54" = alloca [10 x i8]
  store [10 x i8] c"sum = %d\0a\00", [10 x i8]* %".54"
  %".56" = getelementptr [10 x i8], [10 x i8]* %".54", i32 0, i32 0
  %".57" = call i32 (i8*, ...) @"printf"(i8* %".56", i32 %".53")
  ret i32 0
entry.loop_end.loop_update:
  %".49" = load i32, i32* %".34"
  %".50" = add i32 %".49", 1
  store i32 %".50", i32* %".34"
  br label %"entry.loop_end.loop_cond"
}
