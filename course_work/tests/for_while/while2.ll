; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = alloca [32 x i8]
  store [32 x i8] c"While with break and continue:\0a\00", [32 x i8]* %".2"
  %".4" = getelementptr [32 x i8], [32 x i8]* %".2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  %".6" = alloca i32
  store i32 1, i32* %".6"
  %".8" = alloca i32
  store i32 0, i32* %".8"
  br label %"entryloop_do"
entryloop_do:
  br label %"entry.loop_cond"
entry.loop_cond:
  %".12" = load i32, i32* %".8"
  %".13" = icmp slt i32 %".12", 20
  br i1 %".13", label %"entry.loop_body", label %"entry.loop_end"
entry.loop_body:
  %".15" = load i32, i32* %".8"
  %".16" = add i32 %".15", 1
  store i32 %".16", i32* %".8"
  %".18" = load i32, i32* %".8"
  %".19" = srem i32 %".18", 3
  %".20" = icmp eq i32 %".19", 0
  br i1 %".20", label %"entry.loop_body.if", label %"entry.loop_body.else"
entry.loop_end:
  %".43" = load i32, i32* %".6"
  %".44" = alloca [11 x i8]
  store [11 x i8] c"result=%d\0a\00", [11 x i8]* %".44"
  %".46" = getelementptr [11 x i8], [11 x i8]* %".44", i32 0, i32 0
  %".47" = call i32 (i8*, ...) @"printf"(i8* %".46", i32 %".43")
  ret i32 0
entry.loop_update:
  br label %"entry.loop_cond"
entry.loop_body.if:
  %".22" = alloca [11 x i8]
  store [11 x i8] c"continue!\0a\00", [11 x i8]* %".22"
  %".24" = getelementptr [11 x i8], [11 x i8]* %".22", i32 0, i32 0
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24")
  br label %"entry.loop_update"
entry.loop_body.else:
  %".27" = load i32, i32* %".8"
  %".28" = icmp sgt i32 %".27", 10
  br i1 %".28", label %"entry.loop_body.else.if", label %"entry.loop_body.else.else"
entry.loop_body.endif:
  br label %"entry.loop_update"
entry.loop_body.else.if:
  %".30" = alloca [8 x i8]
  store [8 x i8] c"break!\0a\00", [8 x i8]* %".30"
  %".32" = getelementptr [8 x i8], [8 x i8]* %".30", i32 0, i32 0
  %".33" = call i32 (i8*, ...) @"printf"(i8* %".32")
  br label %"entry.loop_end"
entry.loop_body.else.else:
  %".35" = load i32, i32* %".6"
  %".36" = load i32, i32* %".8"
  %".37" = mul i32 %".35", %".36"
  store i32 %".37", i32* %".6"
  br label %"entry.loop_body.else.endif"
entry.loop_body.else.endif:
  br label %"entry.loop_body.endif"
}
