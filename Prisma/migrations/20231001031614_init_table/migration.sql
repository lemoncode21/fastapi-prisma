-- CreateTable
CREATE TABLE "post" (
    "id" SERIAL NOT NULL,
    "post" VARCHAR(100) NOT NULL,
    "description" VARCHAR(255) NOT NULL,

    CONSTRAINT "post_pkey" PRIMARY KEY ("id")
);
