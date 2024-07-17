; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = alloca double
  store double 0x40164432ca57a787, double* %".2"
  %".4" = load double, double* %".2"
  %".5" = alloca [18 x i8]
  store [18 x i8] c"float type: i=%f\0a\00", [18 x i8]* %".5"
  %".7" = getelementptr [18 x i8], [18 x i8]* %".5", i32 0, i32 0
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %".4")
  %".9" = alloca double
  store double 0x4011c703afb7e910, double* %".9"
  %".11" = load double, double* %".9"
  %".12" = alloca [46 x i8]
  store [46 x i8] c"double type (with 3 nums after dot): i2=%.3f\0a\00", [46 x i8]* %".12"
  %".14" = getelementptr [46 x i8], [46 x i8]* %".12", i32 0, i32 0
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", double %".11")
  %".16" = trunc i32 49 to i8
  %".17" = alloca i8
  store i8 %".16", i8* %".17"
  %".19" = load i8, i8* %".17"
  %".20" = alloca [18 x i8]
  store [18 x i8] c"49 as char: j=%c\0a\00", [18 x i8]* %".20"
  %".22" = getelementptr [18 x i8], [18 x i8]* %".20", i32 0, i32 0
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22", i8 %".19")
  %".24" = alloca i32
  store i32 5, i32* %".24"
  %".26" = load i32, i32* %".24"
  %".27" = alloca [16 x i8]
  store [16 x i8] c"int type: k=%d\0a\00", [16 x i8]* %".27"
  %".29" = getelementptr [16 x i8], [16 x i8]* %".27", i32 0, i32 0
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29", i32 %".26")
  %".31" = alloca [5 x i8]
  store [5 x i8] c"5\096\0a\00", [5 x i8]* %".31"
  %".33" = getelementptr [5 x i8], [5 x i8]* %".31", i32 0, i32 0
  %".34" = alloca [23 x i8]
  store [23 x i8] c"Massive of chars s: %s\00", [23 x i8]* %".34"
  %".36" = getelementptr [23 x i8], [23 x i8]* %".34", i32 0, i32 0
  %".37" = call i32 (i8*, ...) @"printf"(i8* %".36", i8* %".33")
  %".38" = getelementptr [5 x i8], [5 x i8]* %".31", i32 0, i32 0
  %".39" = getelementptr [5 x i8], [5 x i8]* %".31", i32 0, i32 2
  %".40" = load i8, i8* %".39"
  %".41" = trunc i32 33 to i8
  store i8 %".41", i8* %".39"
  %".43" = getelementptr [5 x i8], [5 x i8]* %".31", i32 0, i32 0
  %".44" = alloca [32 x i8]
  store [32 x i8] c"Remove s[2] with 33 as char: %s\00", [32 x i8]* %".44"
  %".46" = getelementptr [32 x i8], [32 x i8]* %".44", i32 0, i32 0
  %".47" = call i32 (i8*, ...) @"printf"(i8* %".46", i8* %".43")
  ret i32 0
}
